import pandas as pd
from datetime import date

def NacimientoAedad(df):
    df['DOB'] = pd.to_datetime(df['DOB'], errors='coerce')
    df["Age"] = pd.Timestamp.today() - df["DOB"]
    df["Age"] = (df["Age"].dt.days // 365.25).astype(int)
    print(df["Age"])
    return df