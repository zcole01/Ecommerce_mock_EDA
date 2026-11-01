#imports
import pandas as pd 
import re #regex
import numpy as np #used for 

def clean_data(df):
    df = df.copy()
    #cleaning column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    #list of columns
    strcol = [
        "customer_name","email","phone","city","state","product",
        "category","sales_rep","customer_type","payment_method",
        "order_status"
    ]
    #loop and remove whitespace in columns
    for col in strcol:
        df[col] = df[col].str.strip()
    #standardize names
    df["city"] = df["city"].str.title()
    df["product"] = df["product"].str.title()
    df["sales_rep"] = df["sales_rep"].str.title()
    df["customer_type"] = df["customer_type"].str.capitalize()
    df["category"] = df["category"].str.capitalize()
    df["order_status"] = df["order_status"].str.capitalize()
    #cleaning up data inputs
    df["quantity"] = df["quantity"].abs()
    df["unit_price"] = df["unit_price"].replace(r"[^0-9.]", "", regex=True)#removes non-numeric characters
    df["order_status"] = df["order_status"].replace("Cancelled", "Cancel")
    df["order_status"] = df["order_status"].replace("Completed", "Complete")
    df["payment_method"] = df["payment_method"].replace("CC", "Credit Card")
    df["payment_method"] = df["payment_method"].replace("Debit", "Debit Card")
    df["payment_method"] = df["payment_method"].str.replace(r"\s+", "",regex = True)#removing all whitespace
    df["customer_type"] = df["customer_type"].replace("N", "New")
    df["customer_type"] = df["customer_type"].replace("Y", "N/A")
    # Adjust data types
    df["quantity"] = df["quantity"].astype("Int64")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    df["discount"] = pd.to_numeric(df["discount"], errors="coerce")
    # Format dates
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce").dt.date
    #Standardize phone
    df["phone"] = (df["phone"].str.replace(r"\D", "", regex=True).str[-10:])
    #validate phone number
    df["phone"] = (df["phone"].str[:3]+ "-"+ df["phone"].str[3:6]+ "-"+ df["phone"].str[6:])
    # Fill missing customer names using the email username 
    missNam = (df["customer_name"].isna() & df["email"].notna())#creating matrix of missing names and filled in emails
    # Techniques used for the uniqueness of the dataset
    df.loc[missNam,"customer_name"] = (df.loc[missNam,"email"].str.split("@").str[0].str.replace(r"[._-]+", " ", regex=True).str.title())#extract name
    #loop through columns and fill in in unknown inputs with N/A
    for col in ["city", "phone", "payment_method","email","sales_rep"]:
        df[col] = df[col].fillna("N/A")
    #Adjust invalid inputs to NaN
    df["unit_price"] = df["unit_price"].replace(" ", np.nan)
    df["unit_price"] = df["unit_price"].replace(9999.99, np.nan)
    #removing duplicates
    df = df.drop_duplicates(keep="first")
    #return cleaned dataframe
    return df




