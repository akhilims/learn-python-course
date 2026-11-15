from tabulate import tabulate
rows = [["ERROR", 2], ["INFO", 1]]
headers = ["level", "count"]
table = tabulate(rows, headers=headers)
print(table)
