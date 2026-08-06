import json
from pathlib import Path


def save_to_json(records, csv_file):
    print("=== ETAP LOAD ===")

    csv_path = Path(csv_file)
    output_name = csv_path.stem + ".json"

    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent

    output_file = project_root / "data" / "processed" / output_name

    with open(output_file, "w") as file:
        json.dump(records, file, indent=4)

    print(f"Plik {output_name} został zapisany.")