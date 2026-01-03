# ETL pipeline

This is my first attempt at an ETL pipeline.
I sourced the data from kaggle and split it into 2 equal csv files.

## Extract

- Read the csv into a pandas dataframe

## Transform

- Replaced all empty entries, "ERROR" entries and "UNKNOWN" entries with numpy's NaN type.
- Corrected the data types of columns

## Load

- Loaded the cleaned dataframe to a postgres database.

# Take aways

- I manually changed the filepath for each csv, I think that's fine for now and now sure how I'd do it automatically through just one python script. So in the future definitely going to look into orchestration tools and automating the process.
- Up my transformations from just basic replaces to be more accurate and give further meaning to the data i.e Using means to fill in empty entries.

# Data Source

https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training
