# Best-Selling Video Game Dashboard

An interactive Streamlit dashboard that explores the 100 best-selling video games of all time, showing which publishers and developers are behind the biggest hits.

**Author:** Ethan Rodriguez
**Course:** CIS 3590 – Internship-Ready Software Development

**Live app:** 

---

## Features

- **Interactive slider** – choose how many of the top publishers (3–20) to display.
- **Plotly bar chart** – total sales (millions of units) per publisher, stacked by developer, with a title, axis labels, and legend.
- **Plotly pie chart** – each platform's share of total sales, shown below the bar chart in the Charts tab.
- **Data tab** – the full dataset in a sortable, searchable table, plus publishers and developers ranked by total sales.
- **Insights tab** – key takeaways from the data, explained in plain language.

## Dataset

**File:** `videogamesales.csv` (100 rows)

**Source:** [Wikipedia – List of best-selling video games](https://en.wikipedia.org/wiki/List_of_best-selling_video_games) (accessed 2026-10-28), supplemented with publisher-reported figures for ranks 51–100.

| Column | Description |
|---|---|
| `Rank` | Position in the list (1 = best-selling) |
| `Title` | Game title |
| `Sales_Millions` | Lifetime units sold, in millions |
| `Platforms` | Platform(s) the game was released on |
| `Release_Year` | Year of original release |
| `Developer` | Studio that developed the game |
| `Publisher` | Company that published the game |
| `Source` | Where the sales figure came from |
| `Notes` | Caveats about the figure (ties, combined versions, etc.) |


### Data limitations

- Sales figures are not all measured the same way: some entries combine multiple versions (e.g. *Mario Kart 8 / Deluxe*), while others count a single platform only (e.g. *Marvel's Spider-Man* is PS4 only).
- Some figures are older and likely underestimate current sales (see the `Notes` column).
- *Tetris* is listed with publisher "Various" because its 520M total spans many publishers.
- Rank 52 has slightly higher sales than rank 51 to preserve Wikipedia's ordering for the top 51.

## Getting Started

### Prerequisites

- Python 3.9 or newer

### Installation

```bash
git clone https://github.com/EthanRod267/streamlitDataAppVideoGames.git
cd streamlitDataAppVideoGames
python -m pip install -r requirements.txt
```

### Run the app

```bash
python -m streamlit run game_dashboard.py
```

The app opens in your browser at <http://localhost:8501>.

> **Windows tip:** if `streamlit` is "not recognized as the name of a cmdlet", use `python -m streamlit` as shown above instead of `streamlit` on its own.

## Project Structure

```
streamlitDataAppVideoGames/
├── game_dashboard.py    # Main Streamlit app
├── main_functions.py    # Helper functions
├── videogamesales.csv   # Dataset
├── requirements.txt     # Python dependencies
└── README.md
```

## Built With

- [Streamlit](https://streamlit.io/) – web app framework
- [pandas](https://pandas.pydata.org/) – data manipulation
- [Plotly Express](https://plotly.com/python/plotly-express/) – interactive charts
