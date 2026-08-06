from src.database import get_connection

from src.config import RAW_DATA

parquet_file_path = str(RAW_DATA)

con = get_connection()

def time_analysis():

    # Trips by Hour
    trips_by_hour = con.execute("""
        SELECT
            EXTRACT(HOUR FROM tpep_pickup_datetime) AS hour,
            COUNT(*) AS total_trips
        FROM read_parquet(?)
        GROUP BY hour
        ORDER BY hour
    """, [parquet_file_path]).pl()

    # Trips by Weekday
    trips_by_weekday = con.execute("""
        SELECT
            DAYNAME(tpep_pickup_datetime) AS weekday,
            COUNT(*) AS total_trips
        FROM read_parquet(?)
        GROUP BY weekday
        ORDER BY COUNT(*) DESC
    """, [parquet_file_path]).pl()

    # Average Fare by Hour
    average_fare_by_hour = con.execute("""
        SELECT
            EXTRACT(HOUR FROM tpep_pickup_datetime) AS hour,
            ROUND(AVG(fare_amount), 2) AS average_fare
        FROM read_parquet(?)
        GROUP BY hour
        ORDER BY hour
    """, [parquet_file_path]).pl()

    # Average Tip by Hour
    average_tip_by_hour = con.execute("""
        SELECT
            EXTRACT(HOUR FROM tpep_pickup_datetime) AS hour,
            ROUND(AVG(tip_amount), 2) AS average_tip
        FROM read_parquet(?)
        GROUP BY hour
        ORDER BY hour
    """, [parquet_file_path]).pl()

    # Trips by Month (Optional but useful)
    trips_by_month = con.execute("""
        SELECT
            MONTHNAME(tpep_pickup_datetime) AS month,
            COUNT(*) AS total_trips
        FROM read_parquet(?)
        GROUP BY month
        ORDER BY COUNT(*) DESC
    """, [parquet_file_path]).fetchall()

    print(trips_by_month)

    con.close()

    return {
        "trips_by_hour": trips_by_hour,
        "trips_by_weekday": trips_by_weekday,
        "average_fare_by_hour": average_fare_by_hour,
        "average_tip_by_hour": average_tip_by_hour,
        "trips_by_month": trips_by_month
    }