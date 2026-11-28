# Create Your First SQLite Database in Python
# Every cell of the notebook, in order, as one script (run: python Create_Your_First_SQLite_Database_in_Python.py)

# ## Activate the course virtual environment

# ## Check that sqlite3 comes with Python

# ## Create a database file with sqlite3.connect

import sqlite3
con = sqlite3.connect("power.db")
cur = con.cursor()
print("connected")

# ## Make a table with CREATE TABLE

sql = """
CREATE TABLE states (
code TEXT PRIMARY KEY,
name TEXT,
kind TEXT)
"""
cur.execute(sql)
print("table made")

# ## Save rows with INSERT INTO and commit

ins = "INSERT INTO states VALUES (?, ?, ?)"
cur.execute(ins, ("GJ", "Gujarat", "state"))
cur.execute(ins, ("LA", "Ladakh", "ut"))
con.commit()
print("rows saved")

# ## Read the table back with SELECT *

q = "SELECT * FROM states"
print(cur.execute(q).fetchall())
