import pandas as pd

def format_for_table(data:list):
    df = pd.DataFrame(data)
    headers = list(df.columns)
    values = [row for i, row in df.iterrows()]
    return {"headers": headers, "values":values}
