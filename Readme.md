# Data Cleaning Project

## Project Summary
This project focuses on cleaning and standardizing a messy sales dataset so it is ready for analysis and reporting. The goal is to improve data quality by correcting inconsistencies, formatting fields consistently, and validating values before they are used in downstream analysis.

## Why This Project Matters
In real-world business data, missing values, inconsistent formatting, and invalid entries are common. This project demonstrates how to identify and resolve those issues using Python and pandas. The result is a cleaner, more accurate dataset that is better suited for reporting, analysis, and decision-making.

## Objectives
- Clean inconsistent column names and text values
- Standardize customer, product, and order-related fields
- Fix missing and invalid values
- Normalize phone numbers, dates, and pricing data
- Prepare a reusable data cleaning function for future use

## Tools Used
- Python
- pandas
- NumPy
- Jupyter Notebook
- Excel

## Project Structure
- Data/ — source and cleaned datasets
- Notebook/ — exploratory data cleaning notebook
- Src/clean_data.py — reusable data cleaning script
- Report/ — reporting and data quality summaries
- Readme — project documentation

## Data Cleaning Workflow
The cleaning process includes:

1. Standardizing column names to lowercase snake_case
2. Removing extra whitespace from text fields
3. Standardizing capitalization for names, cities, products, and statuses
4. Cleaning numeric fields and removing non-numeric characters
5. Converting columns to more accurate data types
6. Formatting dates and phone numbers consistently
7. Filling missing values for key fields such as customer names and emails
8. Normalizing inconsistent labels like payment type and order status

## Example Usage

```python
import pandas as pd
from Src.clean_data import clean_data

# df = pd.read_excel("Data/Messy_Dataset_before.xlsx")
# cleaned_df = clean_data(df)
# print(cleaned_df.head())
```

## Key Data Quality Improvements
- missing customer names are derived from email usernames where possible
- inconsistent order statuses are transformed into standard values
- payment methods are normalized into consistent categories
- invalid characters are removed from numeric columns
- phone numbers are reformatted into a standard US format

## Skills Demonstrated
- Data cleaning
- Data validation
- Pandas transformation
- Handling missing data
- Business data standardization

## Project Status
This project is an ongoing portfolio example focused on practical data cleaning and preparation.

## Future Improvements
- add automated validation rules for each column
- produce a formal quality summary report
- create reusable functions for broader dataset types
- expand the project with a dashboard or summary analysis

## Author
This project is part of a personal portfolio focused on analytics, data quality, and business intelligence workflows.
