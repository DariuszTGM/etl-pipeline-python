from extract.extract import read_csv, find_csv_files
from transform.transform import transform_data
from load.load import save_to_json
from analytics.statistics import show_statistics
from config.config import (
    RAW_DATA_FOLDER,
    PROCESSED_DATA_FOLDER,
    ARCHIVE_DATA_FOLDER,
)
from utils.file_manager import create_directories
from utils.file_manager import archive_file
import time



print("=== START ETL PIPELINE ===")
create_directories(
    RAW_DATA_FOLDER,
    PROCESSED_DATA_FOLDER,
    ARCHIVE_DATA_FOLDER
)
start_time = time.perf_counter()

csv_files = find_csv_files()
processed_files = 0

if not csv_files:
    print("Nie znaleziono plików CSV.")
    exit()

for csv_file in csv_files:

    print(f"\nPrzetwarzam plik: {csv_file}")

    data = read_csv(csv_file)

    if not data:
        print("Pomijam plik.")
        continue

    transformed_data = transform_data(data)
    save_to_json(transformed_data, csv_file)

    archive_file(csv_file)

    show_statistics(transformed_data)
    print(f"Zakończono przetwarzanie: {csv_file}")
    processed_files += 1

end_time = time.perf_counter()

print("\n========================")
print("RAPORT ETL")
print("========================")

print(f"Przetworzono plików: {processed_files}")
print(f"Czas wykonania: {end_time - start_time:.3f} s")

print("========================")
