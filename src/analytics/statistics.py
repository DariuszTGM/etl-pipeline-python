from src.utils.logger import logger


def show_statistics(records):
    logger.info("Obliczanie statystyk.")

    total_records = len(records)

    average_price = sum(record["price"] for record in records) / total_records

    total_inventory_value = sum(
        record["price"] * record["quantity"]
        for record in records
    )

    print("\n=========================")
    print("PIPELINE SUMMARY")
    print("=========================")
    print(f"Records: {total_records}")
    print(f"Average price: {average_price:.2f} PLN")
    print(f"Inventory value: {total_inventory_value} PLN")