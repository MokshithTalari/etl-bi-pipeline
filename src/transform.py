import pandas as pd


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Add a revenue column to the DataFrame.

    The revenue column is calculated as units multiplied by price.

    Args:
        df: Input DataFrame with at least 'units' and 'price' columns.

    Returns:
        DataFrame with an additional 'revenue' column.
    """
    df = df.copy()
    if 'units' not in df.columns or 'price' not in df.columns:
        raise KeyError("DataFrame must contain 'units' and 'price' columns")
    df['revenue'] = df['units'] * df['price']
    return df
