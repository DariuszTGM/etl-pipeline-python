from pathlib import Path

print("=== ETAP EXTRACT ===")

current_file = Path(__file__)
print(f"Bieżący plik: {current_file}")

project_root = current_file.parent.parent.parent
print(f"Folder projektu: {project_root}")

csv_file = project_root / "data" / "raw" / "sales.csv"
print(f"Plik CSV: {csv_file}")

with open(csv_file, "r") as file:
    content = file.read()

print(content)