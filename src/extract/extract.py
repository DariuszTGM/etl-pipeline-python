from pathlib import Path


def read_csv():
    print("=== ETAP EXTRACT ===")

    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent

    csv_file = project_root / "data" / "raw" / "sales.csv"

    with open(csv_file, "r") as file:
        lines = file.readlines()

    rows = []

    for line in lines:
        columns = line.strip().split(",")
        rows.append(columns)

    return rows