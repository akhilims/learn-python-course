# Load power data into SQLite and query it
# Every cell of the notebook, in order, as one script (run: python Load_power_data_into_SQLite_and_query_it.py)

# ## Read the power CSV with pandas

import sqlite3
import pandas as pd
con = sqlite3.connect("power.db")
g = pd.read_csv("generation.csv")
print(g.shape)
print(list(g.columns))

# ## Load a table with to_sql and COUNT(*)

g.to_sql("generation", con, index=False)
q = "SELECT COUNT(*) FROM generation"
print(con.execute(q).fetchone())

# ## SQL SELECT, FROM and LIMIT with read_sql

sql = """
SELECT month, state, fuel, gwh
FROM generation
LIMIT 3
"""
print(pd.read_sql(sql, con))

# ## SQL WHERE and AND: filter the rows

sql = """
SELECT state, gwh
FROM generation
WHERE fuel = 'Solar'
AND month = '2025-07'
"""
print(len(pd.read_sql(sql, con)))

# ## ORDER BY DESC: top solar states

sql = """
SELECT state, gwh
FROM generation
WHERE fuel = 'Solar'
AND month = '2025-07'
ORDER BY gwh DESC
LIMIT 3
"""
print(pd.read_sql(sql, con))
