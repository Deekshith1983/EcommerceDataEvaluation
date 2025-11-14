import sqlite3
import pandas as pd
import os

# Database file name
db_name = 'ecom.db'

# Remove existing database if it exists
if os.path.exists(db_name):
    os.remove(db_name)
    print(f"Removed existing {db_name}")

# Create connection to SQLite database
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

print(f"Created database: {db_name}\n")

# Create tables with correct schema
print("Creating tables...")

# Customers table
cursor.execute('''
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    signup_date DATE NOT NULL
)
''')
print("✓ Created customers table")

# Products table
cursor.execute('''
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock_qty INTEGER NOT NULL
)
''')
print("✓ Created products table")

# Orders table
cursor.execute('''
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATE NOT NULL,
    payment_method TEXT NOT NULL,
    total_amount REAL NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
''')
print("✓ Created orders table")

# Order items table
cursor.execute('''
CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    item_price REAL NOT NULL,
    line_total REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
''')
print("✓ Created order_items table")

# Shipping table
cursor.execute('''
CREATE TABLE shipping (
    shipping_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    shipping_date DATE NOT NULL,
    delivery_date DATE NOT NULL,
    shipping_status TEXT NOT NULL,
    courier TEXT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
)
''')
print("✓ Created shipping table")

conn.commit()
print("\nAll tables created successfully!\n")

# Read CSV files and insert data
print("Reading CSV files and inserting data...\n")

# Load customers
customers_df = pd.read_csv('customers.csv')
customers_df.to_sql('customers', conn, if_exists='append', index=False)
print(f"✓ Inserted {len(customers_df)} records into customers table")

# Load products
products_df = pd.read_csv('products.csv')
products_df.to_sql('products', conn, if_exists='append', index=False)
print(f"✓ Inserted {len(products_df)} records into products table")

# Load orders
orders_df = pd.read_csv('orders.csv')
orders_df.to_sql('orders', conn, if_exists='append', index=False)
print(f"✓ Inserted {len(orders_df)} records into orders table")

# Load order_items
order_items_df = pd.read_csv('order_items.csv')
order_items_df.to_sql('order_items', conn, if_exists='append', index=False)
print(f"✓ Inserted {len(order_items_df)} records into order_items table")

# Load shipping
shipping_df = pd.read_csv('shipping.csv')
shipping_df.to_sql('shipping', conn, if_exists='append', index=False)
print(f"✓ Inserted {len(shipping_df)} records into shipping table")

print("\n" + "="*50)
print("DATABASE POPULATION COMPLETE")
print("="*50 + "\n")

# Print row counts from database
print("Row counts in each table:\n")

tables = ['customers', 'products', 'orders', 'order_items', 'shipping']
for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"  {table:15} : {count:4} rows")

print("\n" + "="*50)

# Close connection
conn.close()
print(f"\nDatabase connection closed. Data successfully loaded into {db_name}")
