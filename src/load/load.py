import json


def save_to_json(records):
    print("=== ETAP LOAD ===")

    with open("data/processed/sales.json", "w") as file:
        json.dump(records, file, indent=4)

    print("Plik sales.json został zapisany.")