# Python Course 11.1: SQL AS, UPDATE and DELETE with WHERE in SQLite

The code of this lesson, exactly as typed and run in the video (a lesson in 3 parts).

## Notebooks (one per video part)

- `Create_Your_First_SQLite_Database_in_Python.ipynb`: Create Your First SQLite Database in Python (the same cells as a plain script: `Create_Your_First_SQLite_Database_in_Python.py`)
- `Load_power_data_into_SQLite_and_query_it.ipynb`: Load power data into SQLite and query it (the same cells as a plain script: `Load_power_data_into_SQLite_and_query_it.py`)
- `SQL_AS__UPDATE_and_DELETE_with_WHERE_in_SQLite.ipynb`: SQL AS, UPDATE and DELETE with WHERE in SQLite (the same cells as a plain script: `SQL_AS__UPDATE_and_DELETE_with_WHERE_in_SQLite.py`)

## Setup (once)

You need Python 3.10 or newer and VS Code with the Python and Jupyter extensions. Open a terminal in this folder.

Windows (PowerShell or Command Prompt):

```
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

(PowerShell says running scripts is disabled? Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then activate again.)

macOS / Linux:

```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

requirements.txt pins the exact versions the video ran: ipykernel==7.4.0, pandas==3.1.1.

## Run it

- Notebook: open the `.ipynb` file in VS Code, pick the `.venv` interpreter (top right, Select Kernel) and run the cells from top to bottom.
- Or the whole notebook as one script: `python <name>.py` (Windows) / `python3 <name>.py` (macOS / Linux).
- Part 1, typed in the terminal: `venv\Scripts\activate` (Windows) / `source venv/bin/activate` (macOS / Linux)
- Part 1, typed in the terminal: `python -c "import sqlite3; print('ready')"` (Windows) / `python3 -c "import sqlite3; print('ready')"` (macOS / Linux)
- Run the parts in order: a later part reads files an earlier part made (they are in this folder too).

## Data files

- `generation.csv`: a ready data file the lesson opens (given, not typed in the video)
