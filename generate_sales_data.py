import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

regions_countries = {
    "Europe": ["Germany", "France", "Italy", "Spain", "Netherlands"],
    "Asia": ["India", "Japan", "Singapore"],
    "North America": ["USA", "Canada"]
}

products = {
    "Electronics": {
        "Laptop": 800,
        "Mobile": 300,
        "Tablet": 250,
        "Monitor": 180,
        "Keyboard": 35,
        "Headphones": 40
    },
    "Furniture": {
        "Chair": 60,
        "Desk": 200,
        "Shelf": 120
    },
    "Office Supplies": {
        "Notebook": 5,
        "Pen Set": 3,
        "Printer Paper": 8
    }
}

customer_segments = ["B2B", "B2C"]
sales_channels = ["Online", "Retail", "Partner"]

start_date = datetime(2025, 1, 1)

rows = []

for i in range(1, 501):
    order_id = f"ORD{i:04d}"

    order_date = start_date + timedelta(days=random.randint(0, 180))

    region = random.choice(list(regions_countries.keys()))
    country = random.choice(regions_countries[region])

    product_category = random.choice(list(products.keys()))
    product_name = random.choice(list(products[product_category].keys()))

    unit_price = products[product_category][product_name]
    quantity = random.randint(1, 20)

    revenue = quantity * unit_price

    cost_percentage = random.uniform(0.55, 0.80)
    cost = round(revenue * cost_percentage, 2)

    profit = round(revenue - cost, 2)

    customer_segment = random.choice(customer_segments)
    sales_channel = random.choice(sales_channels)

    rows.append([
        order_id,
        order_date.strftime("%Y-%m-%d"),
        region,
        country,
        product_category,
        product_name,
        quantity,
        unit_price,
        revenue,
        cost,
        profit,
        customer_segment,
        sales_channel
    ])

df = pd.DataFrame(rows, columns=[
    "Order_ID",
    "Order_Date",
    "Region",
    "Country",
    "Product_Category",
    "Product_Name",
    "Quantity",
    "Unit_Price",
    "Revenue",
    "Cost",
    "Profit",
    "Customer_Segment",
    "Sales_Channel"
])

df.to_csv("data/sales_data.csv", index=False)

print("sales_data.csv created successfully")
print(df.head())
print("Rows:", len(df))