# SQL AS, UPDATE and DELETE with WHERE in SQLite
# Every cell of the notebook, in order, as one script (run: python SQL_AS__UPDATE_and_DELETE_with_WHERE_in_SQLite.py)

# ## SQL AS: a clear column name

import sqlite3
import pandas as pd
con = sqlite3.connect("power.db")
sql = """
SELECT month, gwh AS solar_gwh
FROM generation
WHERE state = 'RJ' AND fuel = 'Solar'
ORDER BY month DESC
LIMIT 3
"""
print(pd.read_sql(sql, con))

# ## Add Karnataka to the states table

ins = "INSERT INTO states VALUES (?, ?, ?)"
con.execute(ins, ("KA", "Karnatka", "state"))
con.commit()
q = "SELECT * FROM states"
print(con.execute(q).fetchall())

# ## SQL UPDATE with WHERE: fix a row

fix = "UPDATE states SET name = 'Karnataka'"
fix += " WHERE code = 'KA'"
con.execute(fix)
con.commit()
print(con.execute(q).fetchall())

# ## SQL DELETE with WHERE: remove a row

out = "DELETE FROM states WHERE code = 'KA'"
con.execute(out)
con.commit()
print(con.execute(q).fetchall())
con.close()
