import pandas as pd
from logger import get_logger

logger = get_logger(__name__)

def clean_and_transform(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Cleaning and transforming data...")

    required_columns = ["transaction_id", "date", "customer_id", "amount", "type"]
    df.dropna(subset=required_columns, inplace=True)

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])
    df = df[df["date"].dt.year != 2018]

    df["description"] = df["description"].replace("", pd.NA)
    df.dropna(subset=["description"], inplace=True)

    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df.dropna(subset=["amount"], inplace=True)

    df["amount_category"] = pd.cut(
        df["amount"],
        bins=[-float("inf"), 100, 1000, 5000, float("inf")],
        labels=["small", "medium", "large", "very_large"]
    )

    df["day_of_week"] = df["date"].dt.day_name()

    df.reset_index(drop=True, inplace=True)

    logger.info(f"Transformed data shape: {df.shape}")
    return df
