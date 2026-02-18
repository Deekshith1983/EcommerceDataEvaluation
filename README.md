### Synthetic ecommerce data

### 1. Generated Synthetic E-Commerce Data
Created 5 CSV files with realistic Indian e-commerce data :
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
- Exported reports in multiple formats:
  - **CSV** - Full data export
  - **DOCX** - Professional document with tables and charts
  - **PDF** - Print-ready report with visualizations

**Visualizations Created**:
- 📊 Shipping Status Distribution (Pie Chart)
- 📈 Top 10 Products by Revenue (Bar Chart)

**Output**:
- 1,000 total records
- 205 unique customers
- 438 unique orders
- 98 unique products

### 4. Created Interactive Web Dashboard
**File**: `app.py` + `templates/index.html`

- Built Flask web application with 6 interactive visualizations
- Real-time data analytics dashboard with beautiful UI
- Features:
  - 📊 Shipping Status Distribution (Pie Chart)
  - 💳 Payment Methods Distribution (Donut Chart)
  - 🏆 Top 10 Products by Revenue (Horizontal Bar Chart)
  - 📦 Sales by Category (Bar Chart)
  - 🌆 Top 10 Cities by Orders (Bar Chart)
  - 🚚 Courier Performance Comparison (Grouped Bar Chart)
  - 📈 5 Key Business Statistics Cards
  - 🎨 Gradient background with responsive design


---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git installed on your system
- Internet connection for package installation

### Step 1: Clone the Repository

**For Windows (PowerShell/CMD):**
```bash
git clone https://github.com/Deekshith1983/EcommerceDataEvaluation.git
cd EcommerceDataEvaluation
```

**For Linux/Mac:**
```bash
git clone https://github.com/Deekshith1983/EcommerceDataEvaluation.git
cd EcommerceDataEvaluation
```

### Step 2: Create Virtual Environment

**For Windows:**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**For Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn python-docx reportlab flask plotly
```

Or install specific versions:
```bash
pip install pandas==2.3.3 numpy==2.3.4 flask==3.1.2 plotly==6.4.0 python-docx==1.2.0 reportlab==4.4.4
```

### Step 4: Run the Project

**Option A: Load Data to Database**
```bash
python load_data_to_sqlite.py
```
This will create `ecom.db` and load all CSV data into SQLite tables.

**Option B: Generate Reports**
```bash
python generate_report.py
```
This will generate CSV, DOCX, and PDF reports with visualizations.

**Option C: Launch Web Dashboard** 🌐
```bash
python app.py
```
Then open your browser and navigate to: `http://127.0.0.1:5000`

### Step 5: Explore the Dashboard

Once the Flask server is running, you'll see:
- 📊 6 Interactive Charts
- 📈 5 Key Business Statistics
- 🎨 Beautiful gradient UI with responsive design

Press `Ctrl+C` in the terminal to stop the server.

---

## Tools & Technologies Used

| Tool |  Purpose |
|------|---------|
| **Python** |  Programming language |
| **pandas** |  CSV handling and data operations |
| **SQLite3** |  Database management |
| **numpy** |  Data processing |
| **Flask** |  Web framework for dashboard |
| **Plotly** |  Interactive visualizations |
| **matplotlib** | Static chart generation |
| **seaborn** | Statistical visualizations |
| **python-docx** |  DOCX report generation |
| **reportlab** |  PDF report generation |
| **VS Code** | Development environment |


---

## Project Files

```
Ecommerce-Data/
│
├── customers.csv              # Customer data (501 rows)
├── products.csv               # Product catalog (501 rows)
├── orders.csv                 # Order headers (501 rows)
├── order_items.csv            # Order line items (1,001 rows)
├── shipping.csv               # Shipping details (501 rows)
│
├── ecom.db                    # SQLite database
│
├── load_data_to_sqlite.py     # Database creation & ETL script
├── generate_report.py         # SQL query & reporting script
│
├── app.py                     # Flask web dashboard application
├── templates/
│   └── index.html             # Dashboard HTML template
│
├── ecommerce_report.csv       # Generated CSV report
├── ecommerce_report.docx      # Generated DOCX report
├── ecommerce_report.pdf       # Generated PDF report
│
├── shipping_status_chart.png  # Shipping status pie chart
├── top_products_chart.png     # Top products bar chart
│
├── README.md                  # This file
```
