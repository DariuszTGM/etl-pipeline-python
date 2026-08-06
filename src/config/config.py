from pathlib import Path

CURRENT_FILE = Path(__file__)

PROJECT_ROOT = CURRENT_FILE.parent.parent.parent

RAW_DATA_FOLDER = PROJECT_ROOT / "data" / "raw"

PROCESSED_DATA_FOLDER = PROJECT_ROOT / "data" / "processed"

CSV_PATTERN = "*.csv"

ARCHIVE_DATA_FOLDER = PROJECT_ROOT / "data" / "archive"