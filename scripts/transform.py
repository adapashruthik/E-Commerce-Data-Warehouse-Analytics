import pandas as pd

# ==========================
# Read Raw Datasets
# ==========================

customers = pd.read_csv("../data/raw/olist_customers_dataset.csv")
orders = pd.read_csv("../data/raw/olist_orders_dataset.csv")
order_items = pd.read_csv("../data/raw/olist_order_items_dataset.csv")
products = pd.read_csv("../data/raw/olist_products_dataset.csv")
payments = pd.read_csv("../data/raw/olist_order_payments_dataset.csv")

# ==========================
# Data Transformation
# ==========================

# Create Revenue Column
order_items["revenue"] = (
    order_items["price"] + order_items["freight_value"]
)

# ==========================
# Dimension Tables
# ==========================

dim_customer = customers[
    [
        "customer_id",
        "customer_city",
        "customer_state"
    ]
]

dim_product = products[
    [
        "product_id",
        "product_category_name"
    ]
]

# ==========================
# Fact Table
# ==========================

fact_sales = order_items.merge(
    payments[
        [
            "order_id",
            "payment_value"
        ]
    ],
    on="order_id",
    how="left"
)

# Keep only required columns
fact_sales = fact_sales[
    [
        "order_id",
        "product_id",
        "price",
        "freight_value",
        "revenue",
        "payment_value"
    ]
]

# ==========================
# Save Processed Files
# ==========================

dim_customer.to_csv(
    "../data/processed/dim_customer.csv",
    index=False
)

dim_product.to_csv(
    "../data/processed/dim_product.csv",
    index=False
)

fact_sales.to_csv(
    "../data/processed/fact_sales.csv",
    index=False
)

print("===================================")
print("ETL Process Completed Successfully!")
print("===================================")
print("Dim Customer:", dim_customer.shape)
print("Dim Product :", dim_product.shape)
print("Fact Sales  :", fact_sales.shape)