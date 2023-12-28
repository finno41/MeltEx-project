import pandas as pd
from meltexapp.config.listing import get_listing_title


def format_for_table(
    data: list,
    show_columns,
    update=False,
):
    headers = [{"label": get_listing_title(col), "key": col} for col in show_columns]
    if not data and show_columns:
        return {
            "headers": headers,
            "values": [],
        }
    df = pd.DataFrame(data)
    ids = list(df["id"])
    df = df.drop("id", axis=1)
    df = df[show_columns]
    values = [row for i, row in df.iterrows()]
    values = [(ids[i], r) for i, r in enumerate(values)]
    return {"headers": headers, "values": values}
