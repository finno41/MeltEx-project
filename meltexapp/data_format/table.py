import pandas as pd
from meltexapp.config.listing import get_listing_title


def format_for_table(
    data: list,
    show_columns,
    update=False,
):
    if not data and show_columns:
        return {
            "headers": [get_listing_title(col) for col in show_columns],
            "values": [[]],
        }
    df = pd.DataFrame(data)
    ids = list(df["id"])
    df = df.drop("id", axis=1)
    df = df[show_columns]
    df.columns = [get_listing_title(col) for col in df.columns]
    headers = list(df.columns)
    values = [row for i, row in df.iterrows()]
    values = [(ids[i], r) for i, r in enumerate(values)]
    if update:
        headers.append("")
    return {"headers": headers, "values": values}
