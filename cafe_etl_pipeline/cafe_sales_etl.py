import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os
import sqlalchemy

load_dotenv()
host = os.getenv("DB_HOST")
password = os.getenv("DB_PASSWORD")

FILE_PATH = "dirty_cafe_sales_half2.csv"
DATABASE_URL = f"postgresql://postgres:{password}@{host}:5432/cafe_sales_db"

db_engine = sqlalchemy.create_engine(DATABASE_URL)


def extract(filepath):
    df = pd.read_csv(filepath)
    return df


def transform(dataframe):
    dataframe["Item"] = dataframe["Item"].replace(["ERROR", None, "UNKNOWN"], np.nan)
    dataframe["Quantity"] = dataframe["Quantity"].replace(
        ["ERROR", None, "UNKNOWN"], np.nan
    )
    dataframe["Price Per Unit"] = dataframe["Price Per Unit"].replace(
        ["ERROR", None, "UNKNOWN"], np.nan
    )
    dataframe["Total Spent"] = dataframe["Total Spent"].replace(
        ["ERROR", None, "UNKNOWN"], np.nan
    )
    dataframe["Payment Method"] = dataframe["Payment Method"].replace(
        ["ERROR", None, "UNKNOWN"], np.nan
    )
    dataframe["Location"] = dataframe["Location"].replace(
        ["ERROR", None, "UNKNOWN"], np.nan
    )
    dataframe["Transaction Date"] = dataframe["Transaction Date"].replace(
        ["ERROR", None, "UNKNOWN"], np.nan
    )

    dataframe["Quantity"] = dataframe["Quantity"].astype(float)
    dataframe["Price Per Unit"] = dataframe["Price Per Unit"].astype(float)
    dataframe["Total Spent"] = dataframe["Total Spent"].astype(float)
    dataframe["Transaction Date"] = pd.to_datetime(
        dataframe["Transaction Date"], format="%Y-%m-%d"
    )
    return dataframe


def load(dataframe, engine):
    dataframe.to_sql(
        name="cleaned_cafe_sales", con=engine, if_exists="append", index=False
    )


raw_sales = extract(FILE_PATH)
transformed_sales = transform(raw_sales)
load(transformed_sales, db_engine)
