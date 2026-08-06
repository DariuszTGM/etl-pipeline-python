from src.transform.transform import transform_data


def test_transform_data():
    rows = [
        ["id", "product", "price", "quantity"],
        ["1", "Laptop", "4500", "2"],
        ["2", "Mouse", "80", "5"],
    ]

    result = transform_data(rows)

    assert len(result) == 2
    assert result[0]["product"] == "Laptop"
    assert result[1]["price"] == 80
    assert result[0]["quantity"] == 2

def test_transform_skips_invalid_rows():
    rows = [
        ["id", "product", "price", "quantity"],
        ["1", "Laptop", "4500", "2"],
        ["X", "Mouse", "80", "5"],
    ]

    result = transform_data(rows)

    assert len(result) == 1
    assert result[0]["product"] == "Laptop"

def test_transform_empty_data():
    rows = [
        ["id", "product", "price", "quantity"]
    ]

    result = transform_data(rows)

    assert result == []
    