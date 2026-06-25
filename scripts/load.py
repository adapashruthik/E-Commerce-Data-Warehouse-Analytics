import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = "root"
password = quote_plus("Adapa@123")
host = "localhost"
database = "ecommerce_dw"

engine = create_engine(
    f"mysql+mysqlconnector://{username}:{password}@{host}/{database}"
)

# MySQL Connection


# Read Processed Files
dim_customer = pd.read_csv("../data/processed/dim_customer.csv")
dim_product = pd.read_csv("../data/processed/dim_product.csv")
fact_sales = pd.read_csv("../data/processed/fact_sales.csv")

# Load to MySQL
dim_customer.to_sql(
    "dim_customer",
    con=engine,
    if_exists="replace",
    index=False
)

dim_product.to_sql(
    "dim_product",
    con=engine,
    if_exists="replace",
    index=False
)

fact_sales.to_sql(
    "fact_sales",
    con=engine,
    if_exists="replaces",
    index=False
)

print("Data Loaded Successfully!")