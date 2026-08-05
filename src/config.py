from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

RAW_DATA = ROOT / "data" / "raw" / "yellow_tripdata_2025-01.parquet"

PROCESSED_DIR = ROOT / "data" / "processed" / "cleaned_yellow_tripdata_2025_01.parquet"

REPORT_DIR = ROOT / "data" / "reports"
