# Shopping Cart API

A RESTful shopping-cart backend built with Python and Flask. The project models a basic e-commerce workflow and provides endpoints for managing companies, product categories, products, users, addresses, carts, cart items, payment methods, orders, order items, shipping records, and invoices.

It includes both standard Flask routes and OpenAPI documentation generated with Flask-Smorest.

## Project status

This repository is maintained as a portfolio and learning project. The previously hosted Vercel demo is no longer available because its database is no longer running. To explore the API, run it locally with your own PostgreSQL database.

## Features

- CRUD operations for the main shopping-cart resources
- PostgreSQL persistence through SQLAlchemy
- Request and response schemas with Marshmallow
- Swagger UI and an OpenAPI specification through Flask-Smorest
- Separate route, business-logic, and data-access layers
- Vercel-compatible Python entry point

## Technology

- Python
- Flask
- Flask-Smorest
- SQLAlchemy
- PostgreSQL
- Psycopg
- Marshmallow
- Pytest

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/DannyNguyenCode/shoppingcart_api.git
cd shoppingcart_api/mypythonshoppingcartapi
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the database

Create a `.env` file inside `mypythonshoppingcartapi`:

```env
DATABASE_URL=postgresql://USERNAME:PASSWORD@HOST:5432/DATABASE_NAME
```

Use a PostgreSQL connection string for a database you control. The application currently creates its SQLAlchemy tables when it starts.

### 5. Start the API

```bash
python main.py
```

The local Swagger UI is available at:

```text
http://127.0.0.1:5000/docs
```

The original Flask routes use the `/api` prefix.

## Main resources

- Companies
- Categories
- Products
- Users
- Addresses
- Carts and cart items
- Payment methods
- Orders and order items
- Shipping
- Invoices

## Potential improvements

- Replace integer primary keys with UUIDs
- Add meaningful automated tests
- Introduce versioned database migrations
- Move table creation out of application startup
- Add authentication, authorization, and production-ready validation
