# 🛒 Synthetic E-Commerce Data Evaluation & Analytics Dashboard

This project demonstrates a **complete data pipeline** for a synthetic Indian e-commerce dataset — from **data generation → database creation → reporting → interactive analytics dashboard**.

It showcases **data engineering, SQL analytics, report generation, and dashboard development** using Python.

---

# 🌐 Live Interactive Dashboard

The project is deployed online using **Streamlit Cloud**.

👉 **Open the live dashboard:**
https://ecommercedataevaluation.streamlit.app/

The dashboard allows users to explore the dataset interactively without installing or running the project locally.

### Dashboard Features

* 📊 Shipping Status Distribution
* 💳 Payment Methods Distribution
* 🏆 Top 10 Products by Revenue
* 📦 Sales by Category
* 🌆 Top Cities by Orders
* 🚚 Courier Performance Comparison
* 📈 Key Business Statistics Cards
* 📋 Recent Orders Table

The dashboard is built using **Streamlit + Plotly** and reads data directly from the **SQLite database (`ecom.db`)**.

---

# 📊 Project Overview

## 1. Generated Synthetic E-Commerce Data

Created **5 CSV files** with realistic Indian e-commerce data.

| File            | Records |
| --------------- | ------- |
| customers.csv   | 501     |
| products.csv    | 501     |
| orders.csv      | 501     |
| order_items.csv | 1,001   |
| shipping.csv    | 501     |

---

## 2. Created SQLite Database

**File:** `load_data_to_sqlite.py`

Tasks performed:

* Created **`ecom.db` SQLite database**
* Designed **5 relational tables**
* Implemented **foreign key relationships**
* Loaded CSV data using **pandas**
* Verified data integrity with row counts

### Results

* ✅ 500 customers loaded
* ✅ 500 products loaded
* ✅ 500 orders loaded
* ✅ 1,000 order items loaded
* ✅ 500 shipping records loaded

---

## 3. Generated Comprehensive Report

**File:** `generate_report.py`

A SQL query was written joining all **5 tables using INNER JOIN**.

Reports were generated in multiple formats.

### Output Formats

* CSV
* DOCX
* PDF

### Visualizations Generated

* 📊 Shipping Status Distribution (Pie Chart)
* 📈 Top 10 Products by Revenue (Bar Chart)

### Final Dataset

* **1,000 total records**
* **205 unique customers**
* **438 unique orders**
* **98 unique products**

---

## 4. Created Interactive Web Dashboard

**File:** `app.py`

An interactive analytics dashboard built using **Streamlit and Plotly**.

### Dashboard Visualizations

* 📊 Shipping Status Distribution (Pie Chart)
* 💳 Payment Methods Distribution (Donut Chart)
* 🏆 Top 10 Products by Revenue (Horizontal Bar Chart)
* 📦 Sales by Category (Bar Chart)
* 🌆 Top 10 Cities by Orders (Bar Chart)
* 🚚 Courier Performance Comparison (Grouped Bar Chart)

### Additional Features

* 📈 Business KPI summary cards
* 📋 Recent orders table
* 🎨 Clean responsive layout
* ⚡ Fast interactive charts powered by Plotly

---

# 🚀 Getting Started

## Prerequisites

* Python **3.8 or higher**
* Git installed
* Internet connection for installing packages

---

# Step 1 — Clone the Repository

```bash
git clone https://github.com/Deekshith1983/EcommerceDataEvaluation.git
cd EcommerceDataEvaluation
```

---

# Step 2 — Create Virtual Environment

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# Step 3 — Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn python-docx reportlab plotly streamlit
```

Or install specific versions:

```bash
pip install pandas==2.3.3 numpy==2.3.4 plotly==6.4.0 streamlit==1.45.0 python-docx==1.2.0 reportlab==4.4.4
```

---

# Step 4 — Run the Project

## Option A — Load Data into Database

```bash
python load_data_to_sqlite.py
```

Creates the **SQLite database (`ecom.db`)** and loads all CSV files.

---

## Option B — Generate Reports

```bash
python generate_report.py
```

This generates:

* CSV report
* DOCX report
* PDF report
* Visualization images

---

## Option C — Launch Interactive Dashboard 🌐

```bash
streamlit run app.py
```

Streamlit will start a local server.

Open in browser:

```
http://localhost:8501
```

---

# 🧰 Tools & Technologies Used

| Tool         | Purpose                    |
| ------------ | -------------------------- |
| Python       | Programming language       |
| pandas       | Data manipulation          |
| SQLite3      | Database storage           |
| numpy        | Numerical processing       |
| Streamlit    | Interactive web dashboard  |
| Plotly       | Interactive visualizations |
| matplotlib   | Static charts              |
| seaborn      | Statistical visualizations |
| python-docx  | DOCX report generation     |
| reportlab    | PDF report generation      |
| Git & GitHub | Version control            |
| VS Code      | Development environment    |

---

# 📁 Project Structure

```
EcommerceDataEvaluation
│
├── customers.csv
├── products.csv
├── orders.csv
├── order_items.csv
├── shipping.csv
│
├── ecom.db
│
├── load_data_to_sqlite.py
├── generate_report.py
├── app.py
│
├── ecommerce_report.csv
├── ecommerce_report.docx
├── ecommerce_report.pdf
│
├── shipping_status_chart.png
├── top_products_chart.png
│
├── requirements.txt
├── README.md
```

---

# 📌 Key Learning Outcomes

This project demonstrates:

* Data generation and preprocessing
* SQL joins and relational database design
* ETL pipeline creation
* Automated report generation
* Interactive dashboard development
* Data visualization with Plotly
* Cloud deployment with Streamlit

---

# 👨‍💻 Author

**Deekshith S**

GitHub:
https://github.com/Deekshith1983
