from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
orders = pd.read_csv(ROOT / "data" / "orders.csv", parse_dates=["order_date"])
customers = pd.read_csv(ROOT / "data" / "customers.csv")
products = pd.read_csv(ROOT / "data" / "products.csv")

df = orders.merge(customers, on="customer_id").merge(
    products[["product_id", "product", "category"]], on="product_id"
)
completed = df[df["order_status"] == "Completed"].copy()
completed["revenue"] = completed["quantity"] * completed["unit_price"]

print("Dataset shape:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nOrder status:\n", df["order_status"].value_counts())

total_revenue = completed["revenue"].sum()
completed_orders = completed["order_id"].nunique()
aov = total_revenue / completed_orders
repeat_rate = completed.groupby("customer_id")["order_id"].nunique().gt(1).mean() * 100

print(f"\nTotal revenue: {total_revenue:,.2f}")
print(f"Completed orders: {completed_orders:,}")
print(f"Average order value: {aov:,.2f}")
print(f"Repeat customer rate: {repeat_rate:.2f}%")

print("\nRevenue by category:")
print(completed.groupby("category")["revenue"].sum().sort_values(ascending=False))

monthly = (
    completed.assign(month=completed["order_date"].dt.to_period("M").astype(str))
    .groupby("month")["revenue"].sum()
)

plt.figure(figsize=(8,4.5))
plt.plot(monthly.index, monthly.values, marker="o")
plt.title("Monthly Revenue Trend")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
