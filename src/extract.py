import pandas as pd


def extract(path: str = "data/raw/sales.csv") -> pd.DataFrame:
    """Load the raw sales data from a CSV file.

    Args:
        path: Path to the CSV file containing raw sales data.

    Returns:
        A pandas DataFrame with the contents of the CSV file.
    """
    return pd.read_csv(path)
