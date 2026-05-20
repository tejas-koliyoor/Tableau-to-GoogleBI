import pandas as pd
from pathlib import Path

# ------------------------------------------------------
# Load dataset
# ------------------------------------------------------

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "sales_data.csv"

df = pd.read_csv(DATA_PATH)

print("Data Quality Validation Report")
print("=" * 40)

# ------------------------------------------------------
# Basic dataset overview
# ------------------------------------------------------

print("\n1. Dataset Overview")
print("-" * 40)
print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))
print("Columns:", list(df.columns))

# ------------------------------------------------------
# Missing value check
# ------------------------------------------------------

print("\n2. Missing Value Check")
print("-" * 40)

missing_values = df.isnull().sum()
print(missing_values)

total_missing = missing_values.sum()

if total_missing == 0:
    print("Result: PASSED - No missing values found.")
else:
    print("Result: FAILED - Missing values found.")

# ------------------------------------------------------
# Duplicate Order ID check
# ------------------------------------------------------

print("\n3. Duplicate Order ID Check")
print("-" * 40)

duplicate_orders = df["Order_ID"].duplicated().sum()
print("Duplicate Order IDs:", duplicate_orders)

if duplicate_orders == 0:
    print("Result: PASSED - No duplicate Order IDs found.")
else:
    print("Result: FAILED - Duplicate Order IDs found.")

# ------------------------------------------------------
# Revenue formula validation
# Revenue should equal Quantity * Unit_Price
# ------------------------------------------------------

print("\n4. Revenue Formula Validation")
print("-" * 40)

df["Revenue_Check"] = df["Quantity"] * df["Unit_Price"]
revenue_mismatches = df[df["Revenue"] != df["Revenue_Check"]]

print("Revenue mismatches:", len(revenue_mismatches))

if len(revenue_mismatches) == 0:
    print("Result: PASSED - Revenue formula is correct.")
else:
    print("Result: FAILED - Revenue formula mismatch found.")
    print(revenue_mismatches[["Order_ID", "Quantity", "Unit_Price", "Revenue", "Revenue_Check"]].head())

# ------------------------------------------------------
# Profit formula validation
# Profit should equal Revenue - Cost
# ------------------------------------------------------

print("\n5. Profit Formula Validation")
print("-" * 40)

df["Profit_Check"] = df["Revenue"] - df["Cost"]

# Use rounding because cost/profit may contain decimals
profit_mismatches = df[round(df["Profit"], 2) != round(df["Profit_Check"], 2)]

print("Profit mismatches:", len(profit_mismatches))

if len(profit_mismatches) == 0:
    print("Result: PASSED - Profit formula is correct.")
else:
    print("Result: FAILED - Profit formula mismatch found.")
    print(profit_mismatches[["Order_ID", "Revenue", "Cost", "Profit", "Profit_Check"]].head())

# ------------------------------------------------------
# Date validation
# ------------------------------------------------------

print("\n6. Date Validation")
print("-" * 40)

df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

invalid_dates = df["Order_Date"].isnull().sum()
print("Invalid dates:", invalid_dates)

if invalid_dates == 0:
    print("Result: PASSED - All order dates are valid.")
else:
    print("Result: FAILED - Invalid dates found.")

# ------------------------------------------------------
# Negative value checks
# ------------------------------------------------------

print("\n7. Negative Value Checks")
print("-" * 40)

negative_revenue = (df["Revenue"] < 0).sum()
negative_quantity = (df["Quantity"] < 0).sum()
negative_unit_price = (df["Unit_Price"] < 0).sum()

print("Negative revenue rows:", negative_revenue)
print("Negative quantity rows:", negative_quantity)
print("Negative unit price rows:", negative_unit_price)

if negative_revenue == 0 and negative_quantity == 0 and negative_unit_price == 0:
    print("Result: PASSED - No invalid negative values found.")
else:
    print("Result: FAILED - Negative values found.")

# ------------------------------------------------------
# KPI summary for dashboard validation
# ------------------------------------------------------

print("\n8. KPI Summary")
print("-" * 40)

total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
average_order_value = total_revenue / total_orders
profit_margin = total_profit / total_revenue

print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)
print("Average Order Value:", average_order_value)
print("Profit Margin:", profit_margin)

# ------------------------------------------------------
# Grouped KPI checks
# ------------------------------------------------------

print("\n9. Revenue by Region")
print("-" * 40)
print(df.groupby("Region")["Revenue"].sum().sort_values(ascending=False))

print("\n10. Revenue by Product Category")
print("-" * 40)
print(df.groupby("Product_Category")["Revenue"].sum().sort_values(ascending=False))

print("\nValidation completed successfully.")