import polars as pl

from src.config import RAW_DATA, CLEANED_DIR


def clean_data():
    """
    Read the raw parquet file, clean it and save the cleaned dataset.
    """

    # Read parquet
    df = pl.read_parquet(RAW_DATA)

    # Count rows before cleaning
    raw_rows = df.height

    # Remove duplicate rows
    df = df.unique()

    # Remove invalid records
    df = df.filter(
        (pl.col("fare_amount") > 0)
        & (pl.col("trip_distance") > 0)
        & (pl.col("tpep_pickup_datetime") < pl.col("tpep_dropoff_datetime"))
        & (pl.col("total_amount") > 0)
    )

    # Save cleaned parquet
    df.write_parquet(CLEANED_DIR)

    cleaned_rows = df.height

    removed_rows = raw_rows - cleaned_rows

    return {
    "data": df,
    "raw_rows": raw_rows,
    "cleaned_rows": cleaned_rows,
    "removed_rows": removed_rows,
}