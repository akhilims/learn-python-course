# Python Course 11.2: SQL GROUP BY and HAVING
# Every cell of the notebook, in order, as one script (run: python Python_Course_11_2__SQL_GROUP_BY_and_HAVING.py)

# ## SQL aggregates: COUNT, SUM, AVG with read_sql

import sqlite3
import pandas as pd
con = sqlite3.connect("power.db")
sql = """
SELECT COUNT(*) AS n_rows,
ROUND(SUM(gwh)) AS total,
ROUND(AVG(gwh), 1) AS average
FROM generation
WHERE month LIKE '2024%'
"""
print(pd.read_sql(sql, con))

# ## SQL GROUP BY: one total per fuel

sql = """
SELECT fuel, ROUND(SUM(gwh)) AS total
FROM generation
WHERE month LIKE '2024%'
GROUP BY fuel
ORDER BY total DESC
"""
print(pd.read_sql(sql, con))

# ## CASE WHEN: coal's share of every year

sql = """
SELECT substr(month, 1, 4) AS year,
ROUND(100 * SUM(CASE
WHEN fuel = 'Coal' THEN gwh
ELSE 0 END)/SUM(gwh), 1) AS coal_pct
FROM generation
GROUP BY year
"""
print(pd.read_sql(sql, con))

# ## SQL HAVING: keep the big solar states

sql = """
SELECT state, ROUND(SUM(gwh)) AS solar
FROM generation
WHERE fuel = 'Solar'
AND month LIKE '2024%'
GROUP BY state
HAVING SUM(gwh) > 10000
ORDER BY solar DESC
"""
print(pd.read_sql(sql, con))
