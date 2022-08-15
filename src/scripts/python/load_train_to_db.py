import duckdb
from pathlib import Path

DATA_PATH = Path(__file__).absolute().parent.parent.parent.parent / "data"
RAW_DATA_PATH = DATA_PATH / "raw"

IMPORT_QUERY = f"""
CREATE TABLE train_table AS
SELECT * FROM read_csv_auto('{RAW_DATA_PATH / "train_data.csv"}')
"""

if __name__ == "__main__":
    print("importing data to duckdb...")
    con = duckdb.connect(str(RAW_DATA_PATH / "train_data.db"))
    con.execute(IMPORT_QUERY)
    print("Done!")





