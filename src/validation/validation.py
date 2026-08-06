import pandas as pd

from src.config import FEATURED_DIR


def validate_dataset():
    """
    Validate the processed dataset using Pandas.
    """

    # Read featured dataset
    df = pd.read_parquet(FEATURED_DIR)

    validation = {
        "shape": df.shape,
        "columns": list(df.columns),
        "data_types": df.dtypes,
        "null_values": df.isnull().sum(),
        "duplicate_rows": df.duplicated().sum(),
        "memory_usage_mb": round(df.memory_usage(deep=True).sum() / (1024 ** 2), 2),
        "summary_statistics": df.describe(include="all")
    }

    return validation