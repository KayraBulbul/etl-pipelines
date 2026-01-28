import pandas as pd
import sqlalchemy


def extract(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename)
    return df


def transform(df: pd.DataFrame) -> pd.DataFrame:
    pass


def load(clean_data: pd.DataFrame, engine: sqlalchemy.Engine) -> None:
    pass
