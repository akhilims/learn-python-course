# Python Course 5.2: Paths with pathlib
# Every cell of the notebook, in order, as one script (run: python Python_Course_5_2__Paths_with_pathlib.py)

# Create a Path and read its pieces

from pathlib import Path
p = Path("ghost.txt")
print(p.name, p.suffix)

# Check exists and make a folder with mkdir

print(p.exists())
folder = Path("reports")
folder.mkdir(exist_ok=True)

# Join paths with a slash, write and read text

report = folder / "june.txt"
report.write_text("sales: 10")
print(report.read_text())

# List a folder with iterdir

for item in folder.iterdir():
    print(item.name)
print(folder.name)
