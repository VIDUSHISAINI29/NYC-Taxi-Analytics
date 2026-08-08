from src.config import RAW_DATA
from src.database import get_connection

parquet_file = str(RAW_DATA)


def dataset_overview():
    con = get_connection()
# total rows
    total_rows = con.execute("""
    SELECT COUNT(*) AS total_rows FROM read_parquet(?)
""", [parquet_file]).fetchone()[0]
# columns
    columns  = con.execute("""
    DESCRIBE SELECT * FROM read_parquet(?)
""", [parquet_file]).fetchall()
# total columns
    total_columns = len(columns)
# column names
    column_names = [col[0] for col in columns]
# date_range 
    date_range = con.execute("""
    SELECT MIN(tpep_pickup_datetime) AS min_date, MAX(tpep_pickup_datetime) AS max_date FROM read_parquet(?)
""", [parquet_file]).fetchone()
# Vendor IDs
    vendor_ids = con.execute("""
    SELECT DISTINCT VendorID FROM read_parquet(?)
    ORDER BY VendorID
""", [parquet_file]).fetchall()
# Payment types
    payment_types = con.execute("""
    SELECT DISTINCT payment_type FROM read_parquet(?)
    ORDER BY payment_type
""", [parquet_file]).fetchall()

    vendor_ids = [row[0] for row in vendor_ids]
    payment_types = [row[0] for row in payment_types]

    con.close()

    return{
        "total_rows": total_rows,
        "total_columns": total_columns,
        "column_names": column_names,
        "date_range": date_range,
        "vendor_ids": vendor_ids,
        "payment_types": payment_types
    }
    