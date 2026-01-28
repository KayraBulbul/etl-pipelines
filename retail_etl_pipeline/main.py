from etl import extract, transform, load
from dotenv import load_dotenv
import sqlalchemy
import os

load_dotenv()
host = os.getenv("DB_HOST")
password = os.getenv("DB_PASSWORD")

DATABASE_URL = f"postgresql://postgres:{password}@{host}:5432/retail_sales_db"
db_engine = sqlalchemy.create_engine(DATABASE_URL)
