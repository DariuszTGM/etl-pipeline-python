from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

ENV = os.getenv("ENV", "dev")

CURRENT_FILE = Path(__file__)

PROJECT_ROOT = CURRENT_FILE.parent.parent.parent

RAW_DATA_FOLDER = PROJECT_ROOT / "data" / "raw"

PROCESSED_DATA_FOLDER = PROJECT_ROOT / os.getenv("PROCESSED_DATA_FOLDER", "data/processed")

CSV_PATTERN = "*.csv"

ARCHIVE_DATA_FOLDER = PROJECT_ROOT / os.getenv("ARCHIVE_DATA_FOLDER", "data/archive")