import pandas as pd


def parse_date(value):
    return pd.NaT


def parse_time(value):
        return pd.NaT


def clean_dates(df):
    """Clean mixed date, month and time formats."""
    date_cols=["Joining Date","Attendance Date","Created Date","Payment Date","Pay Month"]

    for col in date_cols:
        if col in df:
            df[col]=df[col].map(parse_date)

    time_cols=["Joining Time","Check In","Check Out"]

    for col in time_cols:
        if col in df:
            df[col]=df[col].map(parse_time)

    return df