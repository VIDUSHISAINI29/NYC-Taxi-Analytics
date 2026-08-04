from src.analysis.overview import dataset_overview
from src.analysis.fare import fare_analysis
from src.analysis.time import time_analysis
from src.analysis.vendor import vendor_analysis
from src.analysis.business import business_overview

    # # Overview

def overview():

    overview = dataset_overview()

    print("=== Dataset Overview ===")

    for key, value in overview.items():
        print(f"{key}: {value}")

    # # FARE

def fare():

    fare_data = fare_analysis()

    print("=== Fare Overview ===")

    for key, value in fare_data.items():
        print(f"{key}: {value}")


    # # TIME

def time():

    time_data = time_analysis()

    print("=== Time Overview ===")

    for key, value in time_data.items():
        print(f"{key}: {value}")

## VENDOR


def vendor():

    vendor_data = vendor_analysis()

    print("=== Vendor Overview ===")

    print(vendor_data)


## Business Insights


def business_insights():

    business_data = business_overview()

    print("=== Business Insights ===")

    for key, value in business_data.items():
           print(f"{key}: {value}")

