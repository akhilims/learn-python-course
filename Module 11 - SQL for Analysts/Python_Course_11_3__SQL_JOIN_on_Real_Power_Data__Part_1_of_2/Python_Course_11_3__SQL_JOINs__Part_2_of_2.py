# Python Course 11.3: SQL JOINs (Part 2 of 2)
# Every cell of the notebook, in order, as one script (run: python Python_Course_11_3__SQL_JOINs__Part_2_of_2.py)

# ## LEFT JOIN: find a state with no rows

import sqlite3
import pandas as pd
con = sqlite3.connect("power.db")
sql = """
SELECT s.name, COUNT(g.gwh) AS n
FROM states s
LEFT JOIN generation g
ON g.state = s.code
GROUP BY s.name
HAVING n = 0
"""
print(pd.read_sql(sql, con))

# ## The missing ON mistake in a JOIN

q = "SELECT COUNT(*) FROM generation JOIN states"
print(con.execute(q).fetchone())
