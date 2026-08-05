from src.transformations.cleaning import clean_data


def transform_data():

    cleaned_df = clean_data()

    print("Cleaning Completed")

    print(cleaned_df)