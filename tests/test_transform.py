import pandas as pd
from src.transform import transform


def test_transform_adds_revenue_column() -> None:
    """Ensure the transform function adds a revenue column correctly."""
    df = pd.DataFrame({'units': [2, 3], 'price': [10, 5]})
    result = transform(df)
    assert 'revenue' in result.columns
    assert result.loc[0, 'revenue'] == 20
    assert result.loc[1, 'revenue'] == 15
