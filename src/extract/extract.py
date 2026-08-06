from pathlib import Path
import glob
from utils.logger import logger

def find_csv_files():
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent

    raw_folder = project_root / "data" / "raw"

    csv_files = glob.glob(str(raw_folder / "*.csv"))

    return csv_files
def read_csv(csv_file):
    print("=== ETAP EXTRACT ===")
    logger.info("Rozpoczynam etap Extract.")

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