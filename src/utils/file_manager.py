import shutil
from pathlib import Path

from config.config import ARCHIVE_DATA_FOLDER


def archive_file(csv_file):
    csv_path = Path(csv_file)

    destination = ARCHIVE_DATA_FOLDER / csv_path.name

    shutil.move(csv_path, destination)

    print(f"Przeniesiono {csv_path.name} do archive.")