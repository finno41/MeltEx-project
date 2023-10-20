import pandas as pd
from meltexapp.config.listing import get_listing_title


def format_for_table(data: list, col_headers=False):
    if not data and col_headers:
        return {"headers": col_headers, "values": [[]]}
    df = pd.DataFrame(data)
    df.columns = [get_listing_title(col) for col in df.columns]
    headers = list(df.columns)
    values = [row for i, row in df.iterrows()]
    return {"headers": headers, "values": values}
