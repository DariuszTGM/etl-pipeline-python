import shutil
from pathlib import Path

from src.config.config import ARCHIVE_DATA_FOLDER


def archive_file(csv_file):
    csv_path = Path(csv_file)

    destination = ARCHIVE_DATA_FOLDER / csv_path.name

    shutil.move(csv_path, destination)

    print(f"Przeniesiono {csv_path.name} do archive.")


def create_directories(*directories):
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)