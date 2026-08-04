from src.database import connection
from src.config import RAW_DATA

parquet_file_pat = str(RAW_DATA)

def business_overview():
    payment_type_stats = connection.execute("""
    SELECT
        payment_type,
        COUNT(*) AS total_trips,
        ROUND(AVG(fare_amount), 2) AS average_fare,
        ROUND(AVG(tip_amount), 2) AS average_tip,
      FROM read_parquet(?)
    GROUP BY payment_type;
""",[parquet_file_pat]).pl()
    
    most_common_pu_location = connection.execute("""
    SELECT PULocationID, COUNT(*) as total_trips
    FROM read_parquet(?)
    GROUP BY PULocationID
    ORDER BY total_trips DESC
    LIMIT 20;
""",[parquet_file_pat]).pl()
    
    most_common_do_location = connection.execute("""
    SELECT DOLocationID, COUNT(*) as total_trips
    FROM read_parquet(?)
    GROUP BY DOLocationID
    ORDER BY total_trips DESC
    LIMIT 20;
""",[parquet_file_pat]).pl()

    airport_vs_non_airport_trips = connection.execute("""
    SELECT COUNT(*) AS total_trips,
        CASE
         WHEN Airport_fee != 0 THEN 'Airport Trip'
         ELSE 'Non-Airport Trip'
         END AS is_airport_trip
    FROM read_parquet(?)
    GROUP BY is_airport_trip;
""",[parquet_file_pat]).pl()

    highest_revenue_location = connection.execute("""
    SELECT PULocationID, SUM(total_amount) AS total_revenue
    FROM read_parquet(?)
    GROUP BY PULocationID
    ORDER BY total_revenue DESC
    LIMIT 1;
""",[parquet_file_pat]).pl()

    return{
        "payment_type_stats": payment_type_stats,
        "most_common_pu_location": most_common_pu_location,
        "most_common_do_location": most_common_do_location,
        "airport_vs_non_airport_trips": airport_vs_non_airport_trips,
        "highest_revenue_location": highest_revenue_location
    }

    
    