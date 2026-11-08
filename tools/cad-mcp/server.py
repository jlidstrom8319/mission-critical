"""CadQuery MCP server.

A small stdio MCP server that builds 3D models with CadQuery and exports them
to STEP, STL or SVG. It replaces the `claude-cad` package on PyPI, which
cannot start because it calls the TypeScript MCP API.

Tools:
  create_primitive         box, sphere, cylinder or cone from numeric sizes
  execute_cadquery_script  run CadQuery Python code in a child process

Models are written to $CAD_OUTPUT_DIR (default: ./cad-output).

Security: execute_cadquery_script runs arbitrary Python with the permissions
of the user running this server. The child process has a timeout, but it is
not a sandbox. Review scripts before approving the tool call.

Requires: cadquery, mcp (1.x or 2.x).
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Literal

try:  # mcp 2.x
    from mcp.server.mcpserver import MCPServer as _Server
    from mcp.server.mcpserver.exceptions import ToolError
except ImportError:  # mcp 1.x
    from mcp.server.fastmcp import FastMCP as _Server
    from mcp.server.fastmcp.exceptions import ToolError

# ToolError messages reach the model; other exceptions are hidden by mcp 2.x.

FORMATS = ("step", "stl", "svg")
Format = Literal["step", "stl", "svg"]
SCRIPT_TIMEOUT_S = int(os.environ.get("CAD_SCRIPT_TIMEOUT", "120"))

mcp = _Server("cadquery")


def _output_dir() -> Path:
    path = Path(os.environ.get("CAD_OUTPUT_DIR", "cad-output")).expanduser().resolve()
    path.mkdir(parents=True, exist_ok=True)
    return path


def _target(name: str, fmt: str) -> Path:
    if fmt not in FORMATS:
        raise ToolError(f"format must be one of {', '.join(FORMATS)}")
    stem = re.sub(r"[^0-9A-Za-z._-]+", "_", name).strip("._-") or "model"
    return _output_dir() / f"{stem}.{fmt}"


def _describe(shape, path: Path) -> dict:
    solid = shape.val()
    bb = solid.BoundingBox()
    return {
        "file": str(path),
        "bounding_box": {"x": bb.xlen, "y": bb.ylen, "z": bb.zlen},
        "volume": solid.Volume(),
    }


@mcp.tool()
def create_primitive(
    shape_type: Literal["box", "sphere", "cylinder", "cone"],
    length: float = 10.0,
    width: float = 10.0,
    height: float = 10.0,
    radius: float = 5.0,
    top_radius: float = 0.0,
    name: str = "model",
    format: Format = "step",
) -> dict:
    """Create a primitive solid centred on the origin and export it.

    box uses length, width, height. sphere uses radius. cylinder uses radius
    and height. cone uses radius (base), top_radius and height. Units are
    whatever the caller intends (CadQuery is unitless; STEP readers assume mm).
    Returns the file path, bounding box and volume.
    """
    import cadquery as cq

    wp = cq.Workplane("XY")
    if shape_type == "box":
        shape = wp.box(length, width, height)
    elif shape_type == "sphere":
        shape = wp.sphere(radius)
    elif shape_type == "cylinder":
        shape = wp.cylinder(height, radius)
    elif shape_type == "cone":
        shape = wp.add(cq.Solid.makeCone(radius, top_radius, height))
    else:
        raise ToolError(f"unknown shape_type: {shape_type}")

    path = _target(name, format)
    cq.exporters.export(shape, str(path))
    return _describe(shape, path)


_RUNNER = r"""
import json, sys
import cadquery as cq
code = sys.stdin.read()
ns = {"cq": cq, "cadquery": cq, "result": None}
exec(compile(code, "<cadquery-script>", "exec"), ns)
result = ns.get("result")
if result is None:
    result = next((v for v in ns.values() if isinstance(v, cq.Workplane)), None)
if result is None:
    raise SystemExit("script did not assign a CadQuery Workplane to `result`")
if isinstance(result, cq.Shape):
    result = cq.Workplane("XY").add(result)
cq.exporters.export(result, sys.argv[1])
solid = result.val()
bb = solid.BoundingBox()
print(json.dumps({"file": sys.argv[1],
                  "bounding_box": {"x": bb.xlen, "y": bb.ylen, "z": bb.zlen},
                  "volume": solid.Volume()}))
"""


@mcp.tool()
def execute_cadquery_script(code: str, name: str = "model", format: Format = "step") -> dict:
    """Run CadQuery Python code and export the resulting model.

    `cq` is pre-imported. Assign the final Workplane (or Shape) to `result`.
    The code runs in a separate Python process with a timeout; it is NOT
    sandboxed and has full access to the machine. Returns the file path,
    bounding box and volume.
    """
    path = _target(name, format)
    try:
        proc = subprocess.run(
            [sys.executable, "-I", "-c", _RUNNER, str(path)],
            input=code,
            capture_output=True,
            text=True,
            timeout=SCRIPT_TIMEOUT_S,
        )
    except subprocess.TimeoutExpired:
        raise ToolError(f"script exceeded {SCRIPT_TIMEOUT_S}s timeout") from None
    if proc.returncode != 0:
        raise ToolError((proc.stderr or proc.stdout).strip()[-4000:])
    return json.loads(proc.stdout.strip().splitlines()[-1])


if __name__ == "__main__":
    mcp.run()
