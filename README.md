# ETL Pipeline in Python

A simple ETL (Extract, Transform, Load) pipeline written in Python.

This project demonstrates how to build a modular data processing pipeline using clean project structure, configuration files, logging, unit tests, and automated file management.

---

# Features

- Extract data from CSV files
- Transform data into Python dictionaries
- Validate input records
- Save processed data as JSON
- Generate summary statistics
- Automatically archive processed CSV files
- Logging support
- Unit tests with pytest
- Modular project architecture

---

# Project Structure

```
ETL_PIPELINE/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── archive/
│
├── src/
│   ├── analytics/
│   ├── config/
│   ├── extract/
│   ├── load/
│   ├── transform/
│   ├── utils/
│   └── main.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# Technologies

- Python 3
- pathlib
- json
- logging
- pytest

---

# How to run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python src/main.py
```

Run tests:

```bash
python -m pytest
```

---

# ETL Flow

```
CSV File
    │
    ▼
Extract
    │
    ▼
Transform
    │
    ▼
Load (JSON)
    │
    ▼
Statistics
    │
    ▼
Archive CSV
```

---

# Example Output

Input:

```
id,product,price,quantity
1,Laptop,4500,2
2,Mouse,80,5
```

Output:

```json
[
    {
        "id": 1,
        "product": "Laptop",
        "price": 4500,
        "quantity": 2
    }
]
```

---

# Testing

The project includes unit tests written with **pytest**.

Current coverage includes:

- successful data transformation
- invalid record handling
- empty input handling

Run all tests:

```bash
python -m pytest
```

---

# Author

Created as part of a Python Data Engineering learning project.