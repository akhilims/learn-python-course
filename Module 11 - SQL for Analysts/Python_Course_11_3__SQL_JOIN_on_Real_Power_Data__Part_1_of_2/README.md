# Python Course 11.3: SQL JOINs

The code of this lesson, exactly as typed and run in the video (a lesson in 2 parts).

## Notebooks (one per video part)

- `Python_Course_11_3__SQL_JOINs__Part_1_of_2.ipynb`: Python Course 11.3: SQL JOINs (Part 1 of 2) (the same cells as a plain script: `Python_Course_11_3__SQL_JOINs__Part_1_of_2.py`)
- `Python_Course_11_3__SQL_JOINs__Part_2_of_2.ipynb`: Python Course 11.3: SQL JOINs (Part 2 of 2) (the same cells as a plain script: `Python_Course_11_3__SQL_JOINs__Part_2_of_2.py`)

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
- Run the parts in order: a later part reads files an earlier part made (they are in this folder too).

## Data files

- `fuels.csv`: a ready data file the lesson opens (given, not typed in the video)
- `states.csv`: a ready data file the lesson opens (given, not typed in the video)
