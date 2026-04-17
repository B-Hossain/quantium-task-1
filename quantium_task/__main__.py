from quantium_task.ingest import combined_sales_frame


def main() -> None:
    sales = combined_sales_frame()
    print("rows:", len(sales))
    print("columns:", list(sales.columns))
    print(sales.head(3).to_string(index=False))


if __name__ == "__main__":
    main()
