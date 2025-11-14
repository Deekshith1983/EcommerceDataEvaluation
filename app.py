from flask import Flask, render_template, jsonify
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('ecom.db')
    return conn

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

@app.route('/')
def index():
    df = get_report_data()
    
    # Calculate statistics
    stats = {
        'total_records': len(df),
        'total_customers': df['customer_name'].nunique(),
        'total_orders': df['order_id'].nunique(),
        'total_products': df['product_name'].nunique(),
        'total_revenue': df['total_amount'].sum()
    }
    
    return render_template('index.html', stats=stats)

@app.route('/api/shipping_status')
def shipping_status():
    df = get_report_data()
    status_counts = df['shipping_status'].value_counts()
    
    fig = px.pie(
        values=status_counts.values,
        names=status_counts.index,
        title='Shipping Status Distribution',
        color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    )
    fig.update_traces(
        textposition='inside', 
        textinfo='percent+label', 
        textfont_size=11,
        hoverinfo='skip'
    )
    fig.update_layout(
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="bottom",
            y=0.05,
            xanchor="left",
            x=0.05
        ),
        autosize=True
    )
    
    return jsonify(fig.to_json())

@app.route('/api/top_products')
def top_products():
    df = get_report_data()
    product_revenue = df.groupby('product_name')['item_price'].sum().sort_values(ascending=False).head(10)
    
    fig = go.Figure(data=[
        go.Bar(
            x=product_revenue.values,
            y=product_revenue.index,
            orientation='h',
            marker_color='#1f4788',
            text=[f'₹{val:,.0f}' for val in product_revenue.values],
            textposition='outside',
            hoverinfo='skip'
        )
    ])
    
    fig.update_layout(
        title='Top 10 Products by Revenue',
        xaxis_title='Total Revenue (₹)',
        yaxis_title='Product Name',
        yaxis={'categoryorder': 'total ascending'},
        showlegend=False,
        autosize=True
    )
    
    return jsonify(fig.to_json())

@app.route('/api/category_sales')
def category_sales():
    df = get_report_data()
    category_revenue = df.groupby('category')['item_price'].sum().sort_values(ascending=False)
    
    fig = px.bar(
        x=category_revenue.index,
        y=category_revenue.values,
        title='Sales by Category',
        labels={'x': 'Category', 'y': 'Revenue (₹)'},
        color=category_revenue.values,
        color_continuous_scale='Blues',
        text=[f'₹{val:,.0f}' for val in category_revenue.values]
    )
    
    fig.update_traces(
        textposition='outside',
        hoverinfo='skip'
    )
    fig.update_layout(
        showlegend=False,
        xaxis_tickangle=-45,
        autosize=True
    )
    
    return jsonify(fig.to_json())

@app.route('/api/city_orders')
def city_orders():
    df = get_report_data()
    city_orders = df.groupby('city')['order_id'].nunique().sort_values(ascending=False).head(10)
    
    fig = px.bar(
        x=city_orders.index,
        y=city_orders.values,
        title='Top 10 Cities by Number of Orders',
        labels={'x': 'City', 'y': 'Number of Orders'},
        color=city_orders.values,
        color_continuous_scale='Viridis',
        text=city_orders.values
    )
    
    fig.update_traces(
        textposition='outside',
        hoverinfo='skip'
    )
    fig.update_layout(
        showlegend=False,
        xaxis_tickangle=-45,
        autosize=True
    )
    
    return jsonify(fig.to_json())

@app.route('/api/payment_methods')
def payment_methods():
    df = get_report_data()
    payment_counts = df.groupby('payment_method')['order_id'].nunique()
    
    fig = px.pie(
        values=payment_counts.values,
        names=payment_counts.index,
        title='Payment Methods Distribution',
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    
    fig.update_traces(
        textposition='inside', 
        textinfo='percent+label', 
        textfont_size=11,
        hoverinfo='skip'
    )
    fig.update_layout(
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="bottom",
            y=0.05,
            xanchor="left",
            x=0.05
        ),
        autosize=True
    )
    
    return jsonify(fig.to_json())

@app.route('/api/courier_performance')
def courier_performance():
    df = get_report_data()
    courier_stats = df.groupby('courier').agg({
        'order_id': 'count',
        'shipping_status': lambda x: (x == 'Delivered').sum()
    })
    courier_stats.columns = ['Total', 'Delivered']
    courier_stats['Delivery_Rate'] = (courier_stats['Delivered'] / courier_stats['Total'] * 100).round(2)
    courier_stats = courier_stats.sort_values('Total', ascending=False)
    
    fig = go.Figure(data=[
        go.Bar(
            name='Total Orders', 
            x=courier_stats.index, 
            y=courier_stats['Total'], 
            marker_color='#4ECDC4',
            text=courier_stats['Total'],
            textposition='outside',
            hoverinfo='skip'
        ),
        go.Bar(
            name='Delivered', 
            x=courier_stats.index, 
            y=courier_stats['Delivered'], 
            marker_color='#45B7D1',
            text=courier_stats['Delivered'],
            textposition='outside',
            hoverinfo='skip'
        )
    ])
    
    fig.update_layout(
        title='Courier Performance (Total Orders vs Delivered)',
        barmode='group',
        xaxis_title='Courier Service',
        yaxis_title='Number of Orders',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        autosize=True,
        xaxis=dict(showticklabels=True),
        yaxis=dict(showticklabels=True)
    )
    
    return jsonify(fig.to_json())

@app.route('/api/recent_orders')
def recent_orders():
    df = get_report_data()
    recent = df.nlargest(10, 'order_date')[['customer_name', 'city', 'product_name', 'total_amount', 'shipping_status', 'order_date']]
    return jsonify(recent.to_dict('records'))

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 E-Commerce Dashboard Starting...")
    print("="*60)
    print("📊 Open your browser and go to: http://127.0.0.1:5000")
    print("="*60 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
