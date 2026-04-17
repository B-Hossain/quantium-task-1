import pandas as pd

from quantium_task.paths import iter_sales_csv_paths


def _strip_currency_to_float(price_series: pd.Series) -> pd.Series:
    cleaned = price_series.str.replace("$", "", regex=False)
    return cleaned.astype(float)


def frame_from_csv(csv_path) -> pd.DataFrame:
    raw = pd.read_csv(csv_path)
    enriched = raw.assign(
        unit_price_usd=lambda d: _strip_currency_to_float(d["price"]),
        source_file=csv_path.name,
    )
    return enriched.assign(
        line_revenue_usd=lambda d: d["unit_price_usd"] * d["quantity"],
    )


def combined_sales_frame() -> pd.DataFrame:
    pieces = [frame_from_csv(p) for p in iter_sales_csv_paths()]
    return pd.concat(pieces, ignore_index=True)
