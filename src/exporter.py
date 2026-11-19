import os

processed_path=r'D:\emp\data\processed\process.csv'
rejected_path=r'D:\emp\data\rejected\rejected.csv'
def export_data(df,processed_path,rejected_path):
    """Save cleaned valid records and rejected records."""
    df.to_csv(processed_path,index=False)

    if rejected_path:
        df.to_csv(rejected_path,index=False)

    
    print("File saved:",processed_path)

import pandas as pd
df = pd.read_csv(r'D:\emp\data\raw\employees.csv')
export_data(df,processed_path,rejected_path)