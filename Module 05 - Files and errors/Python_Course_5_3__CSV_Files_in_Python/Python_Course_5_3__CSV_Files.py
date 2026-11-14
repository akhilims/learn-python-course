# Python Course 5.3: CSV Files
# Every cell of the notebook, in order, as one script (run: python Python_Course_5_3__CSV_Files.py)

# ## Writing rows with csv.writer

import csv
with open("scores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerow(["Asha", 90])
    writer.writerow(["Ben", 75])

# ## Reading rows with csv.reader

with open("scores.csv") as f:
    for row in csv.reader(f):
        print(row)

# ## Reading rows as dictionaries with DictReader

with open("scores.csv") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["score"])
