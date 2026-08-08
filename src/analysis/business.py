from src.database import get_connection
from src.config import FEATURED_DIR

parquet_file_path = str(FEATURED_DIR)


def business_overview():
    con = get_connection()

    payment_type_stats = con.execute("""
    SELECT
       CASE payment_type
            WHEN 1 THEN 'Credit Card'
            WHEN 2 THEN 'Cash'
            WHEN 3 THEN 'No Charge'
            WHEN 4 THEN 'Dispute'
            WHEN 5 THEN 'Unknown'
            WHEN 6 THEN 'Voided'
            ELSE 'Other'
        END AS payment_method,
        COUNT(*) AS total_trips,
        ROUND(AVG(fare_amount), 2) AS average_fare,
        ROUND(AVG(tip_amount), 2) AS average_tip,
      FROM read_parquet(?)
    GROUP BY payment_type;
""",[parquet_file_path]).pl()
    
    most_common_pu_location = con.execute("""
    SELECT PULocationID, COUNT(*) as total_trips
    FROM read_parquet(?)
    GROUP BY PULocationID
    ORDER BY total_trips DESC
    LIMIT 20;
""",[parquet_file_path]).pl()
    
    most_common_do_location = con.execute("""
    SELECT DOLocationID, COUNT(*) as total_trips
    FROM read_parquet(?)
    GROUP BY DOLocationID
    ORDER BY total_trips DESC
    LIMIT 20;
""",[parquet_file_path]).pl()

    airport_vs_non_airport_trips = con.execute("""
    SELECT COUNT(*) AS total_trips,
        CASE
         WHEN Airport_fee != 0 THEN 'Airport Trip'
         ELSE 'Non-Airport Trip'
         END AS is_airport_trip
    FROM read_parquet(?)
    GROUP BY Airport_fee;
""",[parquet_file_path]).pl()

    highest_revenue_location = con.execute("""
    SELECT PULocationID, SUM(total_amount) AS total_revenue
    FROM read_parquet(?)
    GROUP BY PULocationID
    ORDER BY total_revenue DESC
    LIMIT 1;
""",[parquet_file_path]).pl()
    
    total_revenue = con.execute("""
    SELECT ROUND(SUM(total_amount),2) AS total_revenue
    FROM read_parquet(?)
""",[parquet_file_path]).fetchone()[0]

        
    avg_distance = con.execute("""
    SELECT ROUND(AVG(trip_distance * 1.609),2) AS avg_trip_distance_in_km
    FROM read_parquet(?)
""",[parquet_file_path]).fetchone()[0]

    con.close()

    return{
        "payment_type_stats": payment_type_stats,
        "most_common_pu_location": most_common_pu_location,
        "most_common_do_location": most_common_do_location,
        "airport_vs_non_airport_trips": airport_vs_non_airport_trips,
        "highest_revenue_location": highest_revenue_location,
        "total_revenue": total_revenue,
        "avg_distance": avg_distance
    }

    
    