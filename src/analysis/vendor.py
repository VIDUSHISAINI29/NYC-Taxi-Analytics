from src.database import get_connection

from src.config import RAW_DATA

parquet_file_path = str(RAW_DATA)


def vendor_analysis():
    con = get_connection()
    
    vendor_stats =  con.execute("""
    SELECT 
        COUNT(*) AS total_trips, 
        VendorID,
        ROUND(AVG(fare_amount),2) AS avg_fare,
        ROUND(AVG(tip_amount),2) AS avg_tip,
        ROUND(AVG(trip_distance * 1.609),2) AS avg_distance_in_km,
        ROUND(AVG(passenger_count),2) AS avg_passenger_count,
        ROUND(SUM(total_amount),2) AS total_revenue
      FROM read_parquet(?)
    GROUP BY VendorID
    ORDER BY VendorID DESC;
""",[parquet_file_path]).pl()

    con.close()
    

    return vendor_stats