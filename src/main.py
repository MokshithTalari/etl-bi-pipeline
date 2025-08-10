from extract import extract
from transform import transform
from load import load


def main() -> None:
    """Run the ETL pipeline: extract, transform, and load."""
    df = extract()
    transformed = transform(df)
    load(transformed)
    print("Loaded data into data/warehouse/warehouse.db")


if __name__ == "__main__":
    main()
