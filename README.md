# mission-critical

A Customer API built with EnrichMCP and SQLAlchemy.

## Overview

This project provides an AI-friendly API for customer and order data using EnrichMCP, a framework for building Model Context Protocol (MCP) servers that expose data models and relationships.

## Features

- **Customer Management**: Track customer accounts with email and status
- **Order Management**: Store and manage customer orders with pricing and status
- **Relationship Resolution**: Automatic relationship resolution between customers and orders
- **AI-Ready**: Fully compatible with Claude and other AI agents via MCP

## Setup

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
pip install -r requirements.txt
```

### Running the API

```bash
python customer_api.py
```

The API will start and create a SQLite database (`customers.db`) for local development.

## Data Models

### Customer

- `id` (int): Unique customer ID
- `email` (str): Primary email address
- `status` (str): Account status (active, suspended, churned)
- `orders` (list[Order]): All orders placed by this customer
- `display_name` (str): Formatted display name

### Order

- `id` (int): Order ID
- `customer_id` (int): Customer ID
- `total` (float): Order total in USD
- `status` (str): Order status (pending, completed, cancelled)
- `customer` (Customer): Customer who placed this order

## Usage

The API exposes customer and order data for AI agents via the MCP protocol. Agents can:

- Retrieve customer information by ID
- Access all orders for a customer
- Filter orders by status
- Create and update customer records

## Architecture

- **EnrichMCP**: Framework for building MCP servers from data models
- **SQLAlchemy**: ORM for database operations
- **SQLite**: Local database (easily swappable for PostgreSQL)
