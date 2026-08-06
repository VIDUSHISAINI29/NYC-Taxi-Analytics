from src.database import get_connection

from src.config import RAW_DATA

parquet_file = str(RAW_DATA)
con = get_connection()

def fare_analysis():
    fare_data = con.execute("""
    SELECT
    AVG(fare_amount) AS average_fare,
    MEDIAN(fare_amount) AS median_fare,
    MIN(fare_amount) AS min_fare,
    MAX(fare_amount) AS max_fare,
    STDDEV(fare_amount) AS stddev_fare,
FROM read_parquet(?)
""", [parquet_file]).fetchone()


    con.close()
     
    return{
        "average_fare": fare_data[0],
        "median_fare": fare_data[1],
        "min_fare": fare_data[2],
        "max_fare": fare_data[3],
        "stddev_fare": fare_data[4]
    }