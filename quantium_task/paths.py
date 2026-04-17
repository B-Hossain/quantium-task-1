from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent
REPOSITORY_ROOT = PACKAGE_ROOT.parent
DATA_DIRECTORY = REPOSITORY_ROOT / "data"
SALES_FILE_PATTERN = "daily_sales_data_*.csv"


def iter_sales_csv_paths():
    """Yield sorted paths to each daily sales CSV under ``data/``."""
    discovered = sorted(DATA_DIRECTORY.glob(SALES_FILE_PATTERN))
    if not discovered:
        msg = f"No files matching {SALES_FILE_PATTERN!r} under {DATA_DIRECTORY}"
        raise FileNotFoundError(msg)
    yield from discovered
