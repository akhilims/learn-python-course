# Python Course 11.5: DuckDB on CSV and Parquet

The code of this lesson, exactly as typed and run in the video.

## Notebooks (one per video part)

- `Python_Course_11_5__DuckDB_on_CSV_and_Parquet.ipynb`: Python Course 11.5: DuckDB on CSV and Parquet (the same cells as a plain script: `Python_Course_11_5__DuckDB_on_CSV_and_Parquet.py`)

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

requirements.txt pins the exact versions the video ran: duckdb==2.0.1, ipykernel==7.4.0.

## Run it

- Notebook: open the `.ipynb` file in VS Code, pick the `.venv` interpreter (top right, Select Kernel) and run the cells from top to bottom.
- Or the whole notebook as one script: `python <name>.py` (Windows) / `python3 <name>.py` (macOS / Linux).
- Part 1, typed in the terminal: `venv\Scripts\activate` (Windows) / `source venv/bin/activate` (macOS / Linux)
- Part 1, typed in the terminal: `pip install duckdb` (Windows) / `python3 -m pip install duckdb` (macOS / Linux)

## Data files

- `generation.csv`: a ready data file the lesson opens (given, not typed in the video)
- `generation.parquet`: written by the code of Part 1; the copy from the video run is included, so later parts run without it
