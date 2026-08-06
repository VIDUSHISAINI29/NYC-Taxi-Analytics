from src.transformations.cleaning import clean_data
from src.transformations.feature_engineering import feature_engineering


def transform_data():

    cleaned_df = clean_data()

    print("Cleaning Completed")

    print(cleaned_df)


def feature_data():

    featured_df = feature_engineering()

    print("Feature Engineering Completed")

    print(featured_df)