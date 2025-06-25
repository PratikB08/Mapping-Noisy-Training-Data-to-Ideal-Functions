# Mapping Noisy Training Data to Ideal Functions

A Python-based solution that:

- **Ingests** noisy training and ideal function data from CSVs into SQLite
- **Selects** best-fit "ideal" functions for each noisy curve via least-squares (SSE)
- **Maps** test data points to chosen functions under a √2‑threshold rule
- **Visualizes** results with interactive Bokeh plots
- **Includes** unit tests for data loading, SSE computation, and mapping logic

---

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
   - [Command-Line Options](#command-line-options)
   - [Examples](#examples)
5. [Directory Structure](#directory-structure)
6. [Running Tests](#running-tests)
7. [Contributing](#contributing)
8. [License](#license)

---

## Features

- Minimal dependencies: uses only Python’s **standard library** (`csv`, `sqlite3`, `math`, `argparse`, `logging`) plus **Bokeh** for plotting.
- **Argparse**-driven CLI for flexible input/output paths
- **SQLite** back‑end for storing and querying data
- **Unit tests** with `pytest` ensure correctness of core logic
- **Logging** at INFO level for clear runtime feedback

---

## Prerequisites

- Python 3.7 or newer
- **Bokeh** (for visualization)
- **pytest** (for running tests)

Install Bokeh and pytest via pip:

```bash
pip install bokeh pytest
```

---

## Installation

1. **Clone** this repository:

   ```bash
git clone https://github.com/<your-org>/mapping-noisy-data.git
cd mapping-noisy-data
```

2. **(Optional)** Create and activate a virtual environment:

   ```bash
python3 -m venv .venv
source .venv/bin/activate    # macOS/Linux
.venv\Scripts\activate     # Windows
```

3. **Install** dependencies:

   ```bash
pip install -r requirements.txt
```

---

## Usage

### Command-Line Options

```bash
usage: assignment_sqlite.py [-h] --train TRAIN --ideal IDEAL --test TEST
                            [--db DB] [--out OUT]

Map noisy training data to ideal functions and generate visualizations.

optional arguments:
  -h, --help       show this help message and exit
  --train TRAIN    Path to training CSV (with columns: x,y1..y4)
  --ideal IDEAL    Path to ideal functions CSV (with columns: x,y1..y50)
  --test TEST      Path to test CSV (with columns: x,y)
  --db DB          SQLite database file (default: assignment.db)
  --out OUT        Output directory for HTML plots (default: .)
``` 

### Examples

Run the script against the provided datasets:

```bash
python assignment_sqlite.py \
  --train ./data/Train.csv \
  --ideal ./data/Ideal.csv \
  --test  ./data/Test.csv \
  --db    results.db \
  --out   ./outputs
```

After execution, you’ll find two interactive HTML files in `./outputs`:

- `training_vs_ideal.html`
- `test_mapping.html`

---

## Directory Structure

```
mapping-noisy-data/
├── data/
│   ├── Train.csv
│   ├── Ideal.csv
│   └── Test.csv
├── outputs/            ← HTML plots (created by script)
├── assignment_sqlite.py
├── test_assignment.py  ← pytest unit tests
├── requirements.txt    ← project dependencies
└── README.md
```

---

## Running Tests

Execute the `pytest` suite:

```bash
pytest -q
```

You should see all tests pass, verifying CSV loading, SSE computation, and mapping logic.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/YourFeature`
3. **Commit** your changes: `git commit -m "Add some feature"`
4. **Push** to your branch: `git push origin feature/YourFeature`
5. **Open** a Pull Request

Please ensure your code passes existing tests and includes new tests for any added functionality.

---

## License

This project is released under the [MIT License](LICENSE). Feel free to use and modify it under MIT terms.
