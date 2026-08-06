from src.utils.logger import logger


def transform_data(rows):
    print("=== ETAP TRANSFORM ===")
    logger.info("Rozpoczynam etap Transform.")

    headers = rows[0]
    data = rows[1:]

    print("Nagłówki:")
    print(headers)

    print("\nDane:")

    for row in data:
        print(row)

    valid_data = []

    for row in data:
        try:
            row[0] = int(row[0])
            row[2] = int(row[2])
            row[3] = int(row[3])

            valid_data.append(row)

        except ValueError:
            logger.error(f"Błędny rekord: {row}")

    print("\nPo transformacji:")

    for row in valid_data:
        print(row)

    records = []

    for row in valid_data:
        record = {
            "id": row[0],
            "product": row[1],
            "price": row[2],
            "quantity": row[3]
        }

        records.append(record)

    print("\nLista słowników:")

    for record in records:
        print(record)

    logger.info(f"Przetworzono {len(records)} poprawnych rekordów.")

    return records