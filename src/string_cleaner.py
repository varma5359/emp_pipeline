import re
import pandas as pd


def clean_name(value):
    return value.title() if value else pd.NA


def clean_department(value):
    return departments.get(value,value.title())


def clean_strings(df):
    """Clean text fields without changing IDs or numeric information."""

    for col in ["Employee Name","Department Head"]:
        if col in df:
            df[col]=df[col].map(clean_name)

    for col in ["City","Location","Job Title","Shift"]:
        if col in df:
            df[col]=df[col].astype("string").str.strip().str.title()

    if "Gender" in df:
        df["Gender"]=df["Gender"].astype("string").str.strip().str.lower()
        df["Gender"]=df["Gender"].map({
            "m":"Male",
            "male":"Male",
            "f":"Female",
            "female":"Female"
        })

    for col in ["Department","Department Name"]:
        if col in df:
            df[col]=df[col].map(clean_department)

    for col in ["Employment Status","Status","Payment Status"]:
        if col in df:
            df[col]=df[col].astype("string").str.strip().str.title()

    for col in df.select_dtypes(include="object").columns:
        df[col]=df[col].replace(
            ["","unknown","UNKNOWN","Unknown","null","NULL","None","none"],
            pd.NA
        )

    return df