# cadquery MCP server

A small stdio MCP server that builds 3D models with [CadQuery](https://cadquery.readthedocs.io/)
and exports them as STEP, STL or SVG. It is registered for this project in `.mcp.json`.

It replaces the `claude-cad` package on PyPI (0.1.7). That package cannot start with any
version of the Python MCP SDK, because it calls the TypeScript SDK's API
(`Server(info, options)`, `setRequestHandler`).

## Tools

| Tool | What it does |
|---|---|
| `create_primitive` | box, sphere, cylinder or cone from numeric sizes, centred on the origin |
| `execute_cadquery_script` | runs CadQuery Python (`cq` pre-imported; assign the model to `result`) |

Each call writes `<name>.<format>` to `CAD_OUTPUT_DIR` (default `cad-output/`, which is
git-ignored) and returns the file path, bounding box and volume.

## Requirements

```bash
pip install cadquery mcp
```

Works with `mcp` 1.x and 2.x. On Windows, if `python3` is not on PATH, change `command` in
`.mcp.json` to `python` or `py`.

## Security

`execute_cadquery_script` runs arbitrary Python with your user's permissions. It runs in a
separate process with a timeout (`CAD_SCRIPT_TIMEOUT`, default 120 s), but it is **not** a
sandbox. Read the script in the tool-approval prompt before allowing it, and don't add this
tool to an auto-allow list.
