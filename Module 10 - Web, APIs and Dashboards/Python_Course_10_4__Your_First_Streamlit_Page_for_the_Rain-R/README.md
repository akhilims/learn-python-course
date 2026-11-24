# Python Course 10.4: Seven Design Rules and a Plotly Dashboard for the Rain-Ready Desk

The code of this lesson, exactly as typed and run in the video (a lesson in 2 parts).

## Notebooks (one per video part)

- Part 1: `Your_First_Streamlit_Page_for_the_Rain-Ready_Desk.ipynb`: Your First Streamlit Page for the Rain-Ready Desk (the same cells as a plain script: `Your_First_Streamlit_Page_for_the_Rain-Ready_Desk.py`)
- Part 2: `The_Rain-Ready_Desk__design_rules_and_a_Plotly_das.ipynb`: The Rain-Ready Desk: design rules and a Plotly dashboard (the same cells as a plain script: `The_Rain-Ready_Desk__design_rules_and_a_Plotly_das.py`)

## Notes

- `Python_Course_10_4_Part_1__..._notes.pdf` and `Python_Course_10_4_Part_2__..._notes.pdf`: the notes of each video part

## Python files

- `app.py`
- `dash.py`

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

requirements.txt pins the exact versions the video ran: ipykernel==7.4.0, kaleido==1.5.2, nbformat==5.11.1, pandas==3.1.1, plotly==7.1.0, streamlit==1.67.0.

## Run it

- Notebook: open the `.ipynb` file in VS Code, pick the `.venv` interpreter (top right, Select Kernel) and run the cells from top to bottom.
- Or the whole notebook as one script: `python <name>.py` (Windows) / `python3 <name>.py` (macOS / Linux).
- Part 1, typed in the terminal: `venv\Scripts\activate` (Windows) / `source venv/bin/activate` (macOS / Linux)
- Part 1, typed in the terminal: `pip install streamlit` (Windows) / `python3 -m pip install streamlit` (macOS / Linux)
- Part 1, typed in the terminal: `streamlit run app.py` (Windows) / `streamlit run app.py` (macOS / Linux)
- Part 2, typed in the terminal: `venv\Scripts\activate` (Windows) / `source venv/bin/activate` (macOS / Linux)
- Part 2, typed in the terminal: `streamlit run app.py` (Windows) / `streamlit run app.py` (macOS / Linux)
- Part 2, typed in the terminal: `pip install plotly` (Windows) / `python3 -m pip install plotly` (macOS / Linux)
- Part 2, typed in the terminal: `streamlit run dash.py` (Windows) / `streamlit run dash.py` (macOS / Linux)
- Run the parts in order: a later part reads files an earlier part made (they are in this folder too).

## Data files

- `city_rain.csv`: a ready data file the lesson opens (given, not typed in the video)
- `city_rain_week.csv`: a ready data file the lesson opens (given, not typed in the video)
