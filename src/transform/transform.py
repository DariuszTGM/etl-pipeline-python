def transform_data(rows):
    print("=== ETAP TRANSFORM ===")

    headers = rows[0]
    data = rows[1:]

    print("Nagłówki:")
    print(headers)

    print("\nDane:")

    for row in data:
        print(row)

    # Zamiana typów danych
    for row in data:
        row[0] = int(row[0])  # id
        row[2] = int(row[2])  # price
        row[3] = int(row[3])  # quantity

    print("\nPo transformacji:")

    for row in data:
        print(row)

    # Tworzenie listy słowników
    records = []

    for row in data:
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

    return records