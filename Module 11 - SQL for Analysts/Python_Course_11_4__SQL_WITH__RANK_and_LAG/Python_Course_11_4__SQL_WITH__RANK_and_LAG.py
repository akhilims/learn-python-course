# Python Course 11.4: SQL WITH, RANK and LAG
# Every cell of the notebook, in order, as one script (run: python Python_Course_11_4__SQL_WITH__RANK_and_LAG.py)

# ## SQL WITH: a running total of solar

import sqlite3
import pandas as pd
con = sqlite3.connect("power.db")
sql = """
WITH yearly AS (
SELECT substr(month, 1, 4) AS year,
ROUND(SUM(gwh)) AS solar
FROM generation WHERE fuel = 'Solar'
GROUP BY year)
SELECT year, solar,
SUM(solar) OVER (ORDER BY year) AS running
FROM yearly
"""
print(pd.read_sql(sql, con).tail(3))

# ## SQL RANK: the leading solar states

sql = """
WITH t AS (
SELECT state, ROUND(SUM(gwh)) AS solar
FROM generation WHERE fuel = 'Solar'
AND month LIKE '2024%'
GROUP BY state)
SELECT state, solar,
RANK() OVER (ORDER BY solar DESC) AS rnk
FROM t LIMIT 3
"""
print(pd.read_sql(sql, con))

# ## SQL LAG: month-over-month solar in 2025

sql = """
WITH m AS (
SELECT month, ROUND(SUM(gwh)) AS solar
FROM generation WHERE fuel = 'Solar'
AND month >= '2025-04'
GROUP BY month)
SELECT month, solar,
LAG(solar) OVER (ORDER BY month) AS before
FROM m
"""
print(pd.read_sql(sql, con))
