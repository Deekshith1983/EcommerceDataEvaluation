import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

# DATABASE CONNECTION
def get_db_connection():
    conn = sqlite3.connect("ecom.db")
    return conn

# LOAD DATA
@st.cache_data
def get_report_data():
    conn = get_db_connection()
    query = """
    SELECT 
        c.name AS customer_name,
        c.city,
        c.state,
        o.order_id,
        o.order_date,
        o.payment_method,
        p.product_name,
        p.category,
        oi.quantity,
        oi.item_price,
        o.total_amount,
        s.shipping_status,
        s.delivery_date,
        s.courier
    FROM customers c
    INNER JOIN orders o ON c.customer_id = o.customer_id
    INNER JOIN order_items oi ON o.order_id = oi.order_id
    INNER JOIN products p ON oi.product_id = p.product_id
    INNER JOIN shipping s ON o.order_id = s.order_id
    ORDER BY o.order_id, oi.order_item_id
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

df = get_report_data()

# TITLE
st.title("🛒 E-Commerce Analytics Dashboard")

# METRICS
total_records = len(df)
total_customers = df["customer_name"].nunique()
total_orders = df["order_id"].nunique()
total_products = df["product_name"].nunique()
total_revenue = df["total_amount"].sum()

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Total Records", total_records)
c2.metric("Customers", total_customers)
c3.metric("Orders", total_orders)
c4.metric("Products", total_products)
c5.metric("Revenue", f"₹{total_revenue:,.0f}")

st.divider()

# SHIPPING STATUS PIE
status_counts = df["shipping_status"].value_counts()

fig1 = px.pie(
    values=status_counts.values,
    names=status_counts.index,
    title="Shipping Status Distribution"
)

# TOP PRODUCTS
product_revenue = (
    df.groupby("product_name")["item_price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig2 = go.Figure(
    go.Bar(
        x=product_revenue.values,
        y=product_revenue.index,
        orientation="h",
        text=[f"₹{v:,.0f}" for v in product_revenue.values],
        textposition="outside"
    )
)

fig2.update_layout(
    title="Top 10 Products by Revenue",
    yaxis={"categoryorder": "total ascending"}
)

# CATEGORY SALES
category_revenue = (
    df.groupby("category")["item_price"]
    .sum()
    .sort_values(ascending=False)
)

fig3 = px.bar(
    x=category_revenue.index,
    y=category_revenue.values,
    title="Sales by Category",
    text=[f"₹{v:,.0f}" for v in category_revenue.values]
)

# CITY ORDERS
city_orders = (
    df.groupby("city")["order_id"]
    .nunique()
    .sort_values(ascending=False)
    .head(10)
)

fig4 = px.bar(
    x=city_orders.index,
    y=city_orders.values,
    title="Top Cities by Orders",
    text=city_orders.values
)

# PAYMENT METHODS
payment_counts = df.groupby("payment_method")["order_id"].nunique()

fig5 = px.pie(
    values=payment_counts.values,
    names=payment_counts.index,
    hole=0.4,
    title="Payment Methods"
)

# COURIER PERFORMANCE
courier_stats = df.groupby("courier").agg(
    Total=("order_id", "count"),
    Delivered=("shipping_status", lambda x: (x == "Delivered").sum())
)

fig6 = go.Figure()

fig6.add_bar(
    name="Total Orders",
    x=courier_stats.index,
    y=courier_stats["Total"]
)

fig6.add_bar(
    name="Delivered",
    x=courier_stats.index,
    y=courier_stats["Delivered"]
)

fig6.update_layout(
    title="Courier Performance",
    barmode="group"
)

# DASHBOARD LAYOUT
col1, col2 = st.columns(2)
col1.plotly_chart(fig1, use_container_width=True)
col2.plotly_chart(fig5, use_container_width=True)

col3, col4 = st.columns(2)
col3.plotly_chart(fig2, use_container_width=True)
col4.plotly_chart(fig3, use_container_width=True)

col5, col6 = st.columns(2)
col5.plotly_chart(fig4, use_container_width=True)
col6.plotly_chart(fig6, use_container_width=True)

st.divider()

# RECENT ORDERS TABLE
st.subheader("Recent Orders")

df["order_date"] = pd.to_datetime(df["order_date"])

recent = df.sort_values(
    "order_date", ascending=False
).head(10)[
    [
        "customer_name",
        "city",
        "product_name",
        "total_amount",
        "shipping_status",
        "order_date",
    ]
]

st.dataframe(recent, use_container_width=True)
