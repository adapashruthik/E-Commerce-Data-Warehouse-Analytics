🛒 E-Commerce Data Warehouse & Analytics Platform
📌 Overview

This project demonstrates an end-to-end ETL pipeline using Python, Pandas, MySQL, SQLAlchemy, and Power BI. Raw e-commerce datasets are extracted, transformed into a Star Schema Data Warehouse, loaded into MySQL, and visualized through an interactive Power BI dashboard.

🛠 Technologies Used
Python
Pandas
NumPy
MySQL
SQLAlchemy
Power BI
Git & GitHub
VS Code
📂 Dataset
Customers
Orders
Order Items
Products
Payments
🏗 Project Architecture
Raw CSV Files
      │
      ▼
Python ETL (Extract → Transform → Load)
      │
      ▼
Processed CSV Files
      │
      ▼
MySQL Data Warehouse
      │
      ▼
Power BI Dashboard
⭐ Features
Developed an ETL Pipeline to process 112K+ e-commerce records.
Designed a Star Schema with Fact_Sales, Dim_Customer, and Dim_Product tables.
Built interactive Power BI dashboards for revenue, product, and sales analysis.
📁 Project Structure
Ecommerce_Data_Warehouse
│── data/
│── scripts/
│── sql/
│── dashboard/
│── README.md
│── requirements.txt
⚙ Installation
git clone https://github.com/yourusername/E-Commerce-Data-Warehouse-Analytics.git

cd Ecommerce_Data_Warehouse

pip install -r requirements.txt

python scripts/transform.py

python scripts/load.py
📊 Dashboard Insights
Total Revenue
Total Orders
Products Sold
Revenue by Product Category
Top Selling Products
Payment Analysis


OUTPUTS
<img width="1225" height="563" alt="Screenshot " src="https://github.com/user-attachments/assets/659dfcd0-b27c-4f5a-99e9-4e1e733f2497" />
