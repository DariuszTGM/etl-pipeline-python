from config.config import RAW_DATA_FOLDER, CSV_PATTERN
import glob
from utils.logger import logger

def find_csv_files():
    return glob.glob(str(RAW_DATA_FOLDER / CSV_PATTERN))

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