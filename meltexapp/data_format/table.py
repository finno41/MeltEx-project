import pandas as pd
from meltexapp.config.listing import get_listing_title


def format_for_table(data: list, col_headers=False, update=False):
    if not data and col_headers:
        return {"headers": col_headers, "values": [[]]}
    df = pd.DataFrame(data)
    ids = list(df["id"])
    df = df.drop("id", axis=1)
    df.columns = [get_listing_title(col) for col in df.columns]
    headers = list(df.columns)
    values = [row for i, row in df.iterrows()]
    values = [(ids[i], r) for i, r in enumerate(values)]
    if update:
        headers.append("")
    return {"headers": headers, "values": values}
