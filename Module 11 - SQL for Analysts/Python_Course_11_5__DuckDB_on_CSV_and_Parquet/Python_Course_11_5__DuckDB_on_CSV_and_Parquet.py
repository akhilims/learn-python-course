# Python Course 11.5: DuckDB on CSV and Parquet
# Every cell of the notebook, in order, as one script (run: python Python_Course_11_5__DuckDB_on_CSV_and_Parquet.py)

# ## DuckDB: run SQL on a CSV file

import duckdb
sql = """
SELECT fuel, ROUND(SUM(gwh)) AS total
FROM 'generation.csv'
WHERE month LIKE '2024%'
GROUP BY fuel
ORDER BY total DESC
LIMIT 3
"""
print(duckdb.sql(sql).df())

# ## Save a Parquet file with COPY TO

import os
duckdb.sql("""COPY (SELECT * FROM 'generation.csv')
TO 'generation.parquet' (FORMAT parquet)""")
print(os.path.getsize("generation.csv") // 1024)
print(os.path.getsize("generation.parquet") // 1024)

# ## Query a Parquet file and count rows

q = "SELECT COUNT(*) FROM 'generation.parquet'"
print(duckdb.sql(q).fetchall())
