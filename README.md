# 🚀 ETL Pipeline in Python

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Pytest](https://img.shields.io/badge/Tests-3%20Passed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Completed-success)

A simple ETL (Extract, Transform, Load) pipeline written in Python.

The project reads CSV files, transforms the data, saves the output as JSON, calculates basic statistics and archives processed files.

---

# Features

- Read CSV files
- Validate data
- Transform records into Python objects
- Save processed data as JSON
- Calculate basic statistics
- Archive processed CSV files
- Automatic directory creation
- Logging
- Unit tests with Pytest

---

# Project Structure

```text
ETL_PIPELINE
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
├── LICENSE
└── .gitignore
```

---

# Workflow

```
CSV
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
Archive
```

---

# Example Input

```csv
id,product,price,quantity
1,Laptop,4500,2
2,Mouse,80,5
3,Keyboard,250,3
```

---

# Example Output

```json
[
    {
        "id": 1,
        "product": "Laptop",
        "price": 4500,
        "quantity": 2
    },
    {
        "id": 2,
        "product": "Mouse",
        "price": 80,
        "quantity": 5
    }
]
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/DariuszTGM/etl-pipeline-python.git
```

Go to the project folder:

```bash
cd etl-pipeline-python
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run

```bash
python src/main.py
```

---

# Run Tests

```bash
python -m pytest
```

Expected output:

```text
3 passed
```

---

# Technologies

- Python
- JSON
- pathlib
- shutil
- logging
- pytest
- Git
- GitHub

---

# Future Improvements

- SQLite support
- PostgreSQL support
- Docker
- GitHub Actions
- Azure Blob Storage
- Azure SQL Database

---

# Author

**Dariusz Drozdowski**

GitHub:
https://github.com/DariuszTGM

---

# License

This project is licensed under the MIT License.