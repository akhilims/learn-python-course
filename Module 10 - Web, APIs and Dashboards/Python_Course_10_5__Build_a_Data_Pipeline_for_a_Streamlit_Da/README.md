# Python Course 10.5: requirements.txt and GitHub for the Rain-Ready Dashboard

The code of this lesson, exactly as typed and run in the video (a lesson in 3 parts).

## Notebooks (one per video part)

- `Rain-Ready_Dashboard__Filters__Ranking_and_Downloa.ipynb`: Rain-Ready Dashboard: Filters, Ranking and Download (the same cells as a plain script: `Rain-Ready_Dashboard__Filters__Ranking_and_Downloa.py`)
- `Rain-Ready_Dashboard__requirements_txt_and_GitHub.ipynb`: Rain-Ready Dashboard: requirements.txt and GitHub (the same cells as a plain script: `Rain-Ready_Dashboard__requirements_txt_and_GitHub.py`)
- `Rain-Ready_Delivery_Desk__the_data_pipeline.ipynb`: Rain-Ready Delivery Desk: the data pipeline (the same cells as a plain script: `Rain-Ready_Delivery_Desk__the_data_pipeline.py`)

## Python files

- `desk.py`
- `pipeline.py`
- `rain_ready.py`

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

requirements.txt pins the exact versions the video ran: ipykernel==7.4.0, kaleido==1.5.2, nbformat==5.11.1, pandas==3.1.1, plotly==7.1.0, requests==2.34.2, streamlit==1.67.0.

## Run it

- Notebook: open the `.ipynb` file in VS Code, pick the `.venv` interpreter (top right, Select Kernel) and run the cells from top to bottom.
- Or the whole notebook as one script: `python <name>.py` (Windows) / `python3 <name>.py` (macOS / Linux).
- Part 1, typed in the terminal: `venv\Scripts\activate` (Windows) / `source venv/bin/activate` (macOS / Linux)
- Part 1, typed in the terminal: `streamlit run desk.py` (Windows) / `streamlit run desk.py` (macOS / Linux)
- Part 2, typed in the terminal: `venv\Scripts\activate` (Windows) / `source venv/bin/activate` (macOS / Linux)
- Part 2, typed in the terminal: `streamlit run rain_ready.py` (Windows) / `streamlit run rain_ready.py` (macOS / Linux)
- Part 3, typed in the terminal: `venv\Scripts\activate` (Windows) / `source venv/bin/activate` (macOS / Linux)
- Part 3, typed in the terminal: `pip install -r requirements.txt` (Windows) / `python3 -m pip install -r requirements.txt` (macOS / Linux)
- Run the parts in order: a later part reads files an earlier part made (they are in this folder too).

## Data files

- `desk_cities.csv`: a ready data file the lesson opens (given, not typed in the video)
