### Synthetic ecommerce data

### Prompt 1: Data Generation
```
Generate 5 synthetic e-commerce CSV files with at least 500 rows each:

- customers.csv – customer_id, name, email, phone, city, state, signup_date
- products.csv – product_id, product_name, category, price, stock_qty
- orders.csv – order_id, customer_id, order_date, payment_method, total_amount
- order_items.csv – order_item_id, order_id, product_id, quantity, item_price
- shipping.csv – shipping_id, order_id, shipping_date, delivery_date, shipping_status, courier

Ensure the data looks realistic, respects foreign key relations, and uses random but consistent IDs.
```

### Prompt 2: Database Creation & Data Loading
```
Write Python code that:
- Creates a SQLite database named ecom.db
- Creates tables for customers, products, orders, order_items, and shipping with correct schema
- Reads the 5 generated CSV files using pandas
- Inserts all records into SQLite tables using SQLAlchemy or sqlite3
- Prints row counts of each table after insertion
```

### Prompt 3: SQL Query & Reporting
```
Write an SQL query on the ecom.db database that joins customers, orders, order_items, products, and shipping to produce a final report containing:
customer_name, city, order_id, order_date, product_name, quantity, item_price, total_amount, shipping_status, delivery_date.

Ensure all joins are correct and include only matching records.
```

---

## What I Did

### 1. Generated Synthetic E-Commerce Data
Created 5 CSV files with realistic Indian e-commerce data using **GitHub Copilot**:
- **customers.csv** - 501 records
- **products.csv** - 501 records
- **orders.csv** - 501 records
- **order_items.csv** - 1,001 records
- **shipping.csv** - 501 records

### 2. Created SQLite Database
**File**: `load_data_to_sqlite.py`

- Created `ecom.db` database
- Designed 5 tables with proper schema and foreign key relationships
- Loaded all CSV data into SQLite tables using pandas
- Verified data integrity with row counts

**Results**:
- ✅ 500 customers loaded
- ✅ 500 products loaded
- ✅ 500 orders loaded
- ✅ 1,000 order items loaded
- ✅ 500 shipping records loaded

### 3. Generated Comprehensive Report
**File**: `generate_report.py`

- Wrote SQL query joining all 5 tables using INNER JOIN
- Generated final report with 10 columns
- Exported results to `ecommerce_report.csv`

**Output**:
- 1,000 total records
- 205 unique customers
- 438 unique orders
- 98 unique products

---

## Tools & Technologies Used

| Tool | Purpose |
|------|---------|
| **Python** | Programming language |
| **pandas** |  CSV handling and data operations |
| **SQLite3** |  Database management |
| **numpy** |  Data processing |
| **VS Code** |  Development environment |
| **GitHub Copilot** |  AI-powered code generation and assistance |

---

## Project Files

```
Ecommerce-Data/
│
├── customers.csv              # Customer data
├── products.csv               # Product catalog
├── orders.csv                 # Order headers
├── order_items.csv            # Order line items
├── shipping.csv               # Shipping details
│
├── ecom.db                    # SQLite database
│
├── load_data_to_sqlite.py     # Database creation & ETL script
├── generate_report.py         # SQL query & reporting script

```
