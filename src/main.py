from extract.extract import read_csv
from transform.transform import transform_data
from load.load import save_to_json

print("=== START ETL PIPELINE ===")

data = read_csv()

if not data:
    print("Pipeline zatrzymany.")
    exit()

transformed_data = transform_data(data)
save_to_json(transformed_data)