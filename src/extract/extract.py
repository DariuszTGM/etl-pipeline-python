from pathlib import Path
from utils.logger import logger


def read_csv():
    print("=== ETAP EXTRACT ===")
    logger.info("Rozpoczynam etap Extract.")

    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent

    csv_file = project_root / "data" / "raw" / "sales.csv"

    try:
        with open(csv_file, "r") as file:
            lines = file.readlines()

    except FileNotFoundError:
        logger.error(f"Nie znaleziono pliku: {csv_file}")
        return []

    rows = []

    for line in lines:
        columns = line.strip().split(",")
        rows.append(columns)

    logger.info(f"Wczytano {len(rows)-1} rekordów.")

    return rows