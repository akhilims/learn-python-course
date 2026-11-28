# Python Course 11.3: SQL JOINs (Part 1 of 2)
# Every cell of the notebook, in order, as one script (run: python Python_Course_11_3__SQL_JOINs__Part_1_of_2.py)

# ## SQL tables: load state and fuel lists

import sqlite3
import pandas as pd
con = sqlite3.connect("power.db")
con.execute("DROP TABLE states")
s = pd.read_csv("states.csv")
s.to_sql("states", con, index=False)
f = pd.read_csv("fuels.csv")
f.to_sql("fuels", con, index=False)
print(len(s), len(f))

# ## SQL JOIN with ON: full state names

sql = """
SELECT g.state, s.name, g.gwh
FROM generation g
JOIN states s ON g.state = s.code
WHERE g.fuel = 'Solar'
AND g.month = '2025-07'
ORDER BY g.gwh DESC
LIMIT 3
"""
print(pd.read_sql(sql, con))

# ## JOIN the fuels table: clean vs fossil power

sql = """
SELECT f.kind, ROUND(SUM(g.gwh)) AS total
FROM generation g
JOIN fuels f ON g.fuel = f.fuel
WHERE g.month LIKE '2024%'
GROUP BY f.kind
"""
print(pd.read_sql(sql, con))
