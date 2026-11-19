import re
import pandas as pd


def money_to_number(value):
    return number


def clean_numbers(df):
    """Clean numeric, salary, bonus and work-hour columns."""
    money_cols=["Salary","Bonus","Basic Salary","HRA","Allowances","Deductions","Overtime Pay","Net Salary","Annual Budget"]

    for col in money_cols:
        if col in df:
            df[col]=df[col].map(money_to_number)

    numeric_cols=["Age","Employee Count","Work Hours","Overtime Hours"]

    for col in numeric_cols:
        if col in df:
            df[col]=pd.to_numeric(df[col],errors="coerce")

    if "Age" in df:
        df.loc[~df["Age"].between(18,65),"Age"]=pd.NA

    if "Employee Count" in df:
        df.loc[df["Employee Count"]<0,"Employee Count"]=pd.NA

    if "Work Hours" in df:
        df.loc[~df["Work Hours"].between(0,24),"Work Hours"]=pd.NA

    if "Overtime Hours" in df:
        df.loc[df["Overtime Hours"]<0,"Overtime Hours"]=pd.NA

    return df