import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('ecom.db')

# SQL query to join all tables
query = """
SELECT 
    c.name AS customer_name,
    c.city,
    o.order_id,
    o.order_date,
    p.product_name,
    oi.quantity,
    oi.item_price,
    o.total_amount,
    s.shipping_status,
    s.delivery_date
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id
INNER JOIN shipping s ON o.order_id = s.order_id
ORDER BY o.order_id, oi.order_item_id
"""

print("Executing SQL query to generate comprehensive e-commerce report...\n")
print("="*80)
print("SQL QUERY:")
print("="*80)
print(query)
print("="*80 + "\n")

# Execute query and fetch results
df = pd.read_sql_query(query, conn)

print(f"Query executed successfully!")
print(f"Total records retrieved: {len(df)}\n")

# Display first 20 rows
print("="*80)
print("SAMPLE REPORT (First 20 rows):")
print("="*80)
print(df.head(20).to_string(index=False))

print("\n" + "="*80)
print("REPORT STATISTICS:")
print("="*80)
print(f"Total Records: {len(df)}")
print(f"Unique Customers: {df['customer_name'].nunique()}")
print(f"Unique Orders: {df['order_id'].nunique()}")
print(f"Unique Products: {df['product_name'].nunique()}")
print(f"\nShipping Status Distribution:")
print(df['shipping_status'].value_counts().to_string())



# Close connection
conn.close()
print("\nDatabase connection closed.")
