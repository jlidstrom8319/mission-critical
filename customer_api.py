"""Customer API using EnrichMCP and SQLAlchemy."""

from enrichmcp import EnrichMCP
from enrichmcp.sqlalchemy import (
    include_sqlalchemy_models,
    sqlalchemy_lifespan,
    EnrichSQLAlchemyMixin,
)
from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase, EnrichSQLAlchemyMixin):
    """SQLAlchemy declarative base with EnrichMCP mixin."""
    pass


class Customer(Base):
    """Represents a customer account."""

    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True, info={"description": "Unique customer ID"})
    email: Mapped[str] = mapped_column(unique=True, info={"description": "Primary email address"})
    status: Mapped[str] = mapped_column(
        default="active",
        info={"description": "Account status", "examples": ["active", "suspended", "churned"]}
    )
    orders: Mapped[list["Order"]] = relationship(
        back_populates="customer",
        info={"description": "All orders placed by this customer"}
    )

    @property
    def display_name(self) -> str:
        """Format for UI display."""
        return f"Customer #{self.id}"


class Order(Base):
    """Represents a customer order."""

    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, info={"description": "Order ID"})
    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id"),
        info={"description": "Customer ID"}
    )
    total: Mapped[float] = mapped_column(info={"description": "Order total in USD"})
    status: Mapped[str] = mapped_column(
        default="pending",
        info={"description": "Order status"}
    )
    customer: Mapped[Customer] = relationship(
        back_populates="orders",
        info={"description": "Customer who placed this order"}
    )


# Create async engine (SQLite for local development, PostgreSQL for production)
engine = create_async_engine(
    "sqlite+aiosqlite:///./customers.db",
    echo=False,
    future=True,
)


# Create the MCP app
app = EnrichMCP(
    "Customer API",
    "Customer data for AI agents",
    lifespan=sqlalchemy_lifespan(Base, engine, cleanup_db_file=True),
)

# Include SQLAlchemy models as MCP resources
include_sqlalchemy_models(app, Base)


if __name__ == "__main__":
    app.run()
