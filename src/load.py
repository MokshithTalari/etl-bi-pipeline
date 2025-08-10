import sqlite3
import pandas as pd
from pathlib import Path


def load(df: pd.DataFrame, db_path: str = "data/warehouse/warehouse.db", table_name: str = "fact_sales") -> None:
    """Load the DataFrame into a SQLite database table.

    Args:
        df: DataFrame containing the transformed data.
        db_path: Path to the SQLite database file.
        table_name: Name of the table to write into the database.
    """
    # Ensure directory exists
    db_file = Path(db_path)
    db_file.parent.mkdir(parents=True, exist_ok=True)
    # Connect to database and load data
    conn = sqlite3.connect(db_path)
    try:
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.commit()
    finally:
        conn.close()
