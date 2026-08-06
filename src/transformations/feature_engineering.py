import polars as pl

from src.config import (
    CLEANED_DIR,
    FEATURED_DIR
)


def feature_engineering():
    """
    Create new features from the cleaned dataset.
    """

    df = pl.read_parquet(CLEANED_DIR)

    df = df.with_columns(

        # Trip duration in minutes
        (
            (
                pl.col("tpep_dropoff_datetime")
                - pl.col("tpep_pickup_datetime")
            )
            .dt.total_minutes()
        ).alias("trip_duration_minutes"),

        # Fare per mile
        (
            pl.col("fare_amount")
            / pl.col("trip_distance")
        ).round(2).alias("fare_per_mile"),

        # Tip percentage
        (
            (
                pl.col("tip_amount")
                / pl.col("fare_amount")
            ) * 100
        ).round(2).alias("tip_percentage"),

        # Weekend trip
        (
            pl.col("tpep_pickup_datetime")
            .dt.weekday()
            >= 5
        ).alias("is_weekend"),

        # Night trip (10 PM – 6 AM)
        (
            (pl.col("tpep_pickup_datetime").dt.hour() >= 22)
            |
            (pl.col("tpep_pickup_datetime").dt.hour() < 6)
        ).alias("is_night_trip"),

        # Airport trip
        (
            pl.col("Airport_fee") > 0
        ).alias("is_airport_trip")

    )

    # Average Speed (mph)
    df = df.with_columns(
        (
            pl.col("trip_distance")
            /
            (pl.col("trip_duration_minutes") / 60)
        ).round(2).alias("average_speed")
    )

    df.write_parquet(FEATURED_DIR)

    return df