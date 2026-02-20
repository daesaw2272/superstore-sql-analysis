from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
EXPORTS = ROOT / "exports"
CHARTS = ROOT / "charts"

CHARTS.mkdir(exist_ok=True)

# ---------- Profit by Region ----------
region = pd.read_csv(EXPORTS / "region_performance.csv")
region.columns = region.columns.str.lower()
region = region.sort_values("profit", ascending=False)

plt.figure()
plt.bar(region["region"], region["profit"])
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig(CHARTS / "profit_by_region.png")
plt.close()

# ---------- Monthly Trends ----------
monthly = pd.read_csv(EXPORTS / "monthly_trend.csv")
monthly.columns = monthly.columns.str.lower()
monthly["month"] = pd.to_datetime(monthly["month"])
monthly = monthly.sort_values("month")

plt.figure()
plt.plot(monthly["month"], monthly["sales"])
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(CHARTS / "monthly_sales_trend.png")
plt.close()

plt.figure()
plt.plot(monthly["month"], monthly["profit"])
plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig(CHARTS / "monthly_profit_trend.png")
plt.close()

# ---------- Bottom 10 Sub-categories ----------
subcat = pd.read_csv(EXPORTS / "subcategory_profit.csv")
subcat.columns = subcat.columns.str.lower()
subcat["label"] = subcat["category"] + " - " + subcat["sub_category"]
worst = subcat.sort_values("profit").head(10)

plt.figure()
plt.bar(worst["label"], worst["profit"])
plt.title("Bottom 10 Sub-Categories by Profit")
plt.xlabel("Sub-Category")
plt.ylabel("Profit")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(CHARTS / "bottom_10_subcategories_profit.png")
plt.close()

# ---------- Top Customers ----------
customers = pd.read_csv(EXPORTS / "top_customers_profit.csv")
customers.columns = customers.columns.str.lower()

plt.figure()
plt.bar(customers["customer_name"], customers["total_profit"])
plt.title("Top 10 Customers by Profit")
plt.xlabel("Customer")
plt.ylabel("Profit")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(CHARTS / "top_customers_by_profit.png")
plt.close()

print("✅ Charts generated successfully in /charts")