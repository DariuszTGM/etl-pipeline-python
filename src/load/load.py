import json
from pathlib import Path

from src.config.config import PROCESSED_DATA_FOLDER


def save_to_json(records, csv_file):
    print("=== ETAP LOAD ===")

    csv_path = Path(csv_file)
    output_name = csv_path.stem + ".json"

    output_file = PROCESSED_DATA_FOLDER / output_name

    with open(output_file, "w") as file:
        json.dump(records, file, indent=4)

    print(f"Plik {output_name} został zapisany.")