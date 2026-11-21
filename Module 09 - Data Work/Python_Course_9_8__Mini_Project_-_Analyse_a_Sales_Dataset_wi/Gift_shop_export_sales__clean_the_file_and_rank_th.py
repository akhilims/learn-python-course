# Gift shop export sales: clean the file and rank the countries
# Every cell of the notebook, in order, as one script (run: python Gift_shop_export_sales__clean_the_file_and_rank_th.py)

# ## Load the Excel sales file with read_excel

import pandas as pd
import matplotlib.pyplot as plt
orders = pd.read_excel("retail_abroad.xlsx")

# ## Check the shape and the bad rows

print(orders.shape)
print((orders["Quantity"] <= 0).sum())
print((orders["UnitPrice"] <= 0).sum())

# ## Clean the data, add Sales, save sales_clean.csv

good = orders[orders["Quantity"] > 0]
good = good[good["UnitPrice"] > 0].copy()
price = good["UnitPrice"]
good["Sales"] = good["Quantity"] * price
print(len(good), round(good["Sales"].sum()))
good.to_csv("sales_clean.csv", index=False)

# ## Group by country and rank the sales

top = good.groupby("Country")["Sales"].sum()
top = top.sort_values().tail(8) / 1000
print(top.round())

# ## Ranked horizontal bar chart with barh and bar_label

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(top.index, top, color="teal")
bars[-1].set_color("darkorange")
ax.bar_label(bars, fmt="%.0f", padding=4)
ax.set_title("Top 8 export countries")
ax.set_xlabel("Sales in thousand pounds")
ax.spines[["top", "right"]].set_visible(False)
src = "Source: UCI Online Retail"
fig.text(0.99, 0.96, src, ha="right")
fig.tight_layout()
plt.show()

# ## Monthly sales table with to_period and pivot_table

good["Month"] = good["InvoiceDate"].dt.to_period("M")
year = good[good["Month"] < "2011-12"]
four = ["Netherlands", "EIRE", "Germany", "France"]
part = year[year["Country"].isin(four)]
table = part.pivot_table("Sales", "Month", "Country", "sum")
table = table[four] / 1000
print(table.round().tail(3))
table.to_csv("monthly.csv")
