# Python Course 9.8: Mini Project - Analyse a Sales Dataset with 3 Charts (Part 2 of 2)
# Every cell of the notebook, in order, as one script (run: python Python_Course_9_8__Mini_Project_-_Analyse_a_Sales.py)

# ## Load the clean sales file and monthly table

import pandas as pd
import matplotlib.pyplot as plt
# Only retail_abroad.xlsx is given, so build sales_clean.csv and monthly.csv from it first
name = "retail_abroad.xlsx"
dates = ["InvoiceDate"]
raw = pd.read_excel(name, parse_dates=dates)
raw = raw.rename(columns={"Invoice": "InvoiceNo", "Price": "UnitPrice"})
raw["InvoiceNo"] = raw["InvoiceNo"].astype(str)
keep = (~raw["InvoiceNo"].str.startswith("C")) & (raw["Quantity"] > 0) & (raw["UnitPrice"] > 0)
clean = raw[keep].dropna(subset=["InvoiceDate"]).copy()
clean["Sales"] = clean["Quantity"] * clean["UnitPrice"]
clean.to_csv("sales_clean.csv", index=False)
clean["Month"] = pd.to_datetime(clean["InvoiceDate"]).dt.to_period("M").astype(str)
monthly = clean.pivot_table("Sales", "Month", "Country", "sum", fill_value=0) / 1000
monthly = monthly[monthly.sum().nlargest(5).index]
monthly.to_csv("monthly.csv")

good = pd.read_csv("sales_clean.csv", parse_dates=dates)
table = pd.read_csv("monthly.csv", index_col=0)
print(good.shape)
print(table.round(1).head())

# ## Stacked area chart: export sales per month

fig, ax = plt.subplots(figsize=(10, 5))
months = table.index.astype(str)
ax.stackplot(months, table.T.values, labels=table.columns, alpha=0.85)
ax.set_title("Export sales per month")
ax.set_ylabel("Sales in thousand pounds")
ax.tick_params(axis="x", rotation=45)
ax.legend(loc="upper left")
src = "Source: UCI Online Retail"
fig.text(0.99, 0.96, src, ha="right")
fig.tight_layout()
plt.show()

# ## Count orders by weekday and hour with pivot_table

import calendar
days = list(calendar.day_name)
good["Day"] = good["InvoiceDate"].dt.day_name()
good["Hour"] = good["InvoiceDate"].dt.hour
one = good.drop_duplicates("InvoiceNo")
busy = one.pivot_table("InvoiceNo", "Day", "Hour", "count")
busy = busy.reindex(days).fillna(0)
print(busy.sum(axis=1))

# ## Heatmap with imshow, colour bar and saved PNG

fig, ax = plt.subplots(figsize=(10, 4))
img = ax.imshow(busy.values, cmap="YlOrRd", aspect="auto")
ax.set_xticks(range(len(busy.columns)), busy.columns)
ax.set_yticks(range(7), days)
ax.set_title("Orders by weekday and hour")
ax.set_xlabel("Hour of the day")
fig.colorbar(img, label="Orders")
src = "Source: UCI Online Retail"
fig.text(0.99, 0.96, src, ha="right")
fig.tight_layout()
plt.savefig("orders_heatmap.png", dpi=120)
plt.show()
