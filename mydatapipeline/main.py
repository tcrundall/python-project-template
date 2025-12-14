import sys

import pandas as pd

from mydatapipeline import (
    analyzer,
    cleaner,
    configloader,
)

COLUMN_MAPPINGS_KEY = "column-mappings"

USAGE = """
        Usage: python main.py my-config-file.json my-data.xlsx
        """

if __name__ == "__main__":
    # ----------------------------------------
    #      Parse and validate user input
    # ----------------------------------------
    if len(sys.argv) != 3:
        print(USAGE)
        sys.exit(1)

    config_file = sys.argv[1]
    excel_file = sys.argv[2]

    if config_file.split(".")[-1] != "json":
        print("Expected a json file as first argument")
        print(USAGE)
        sys.exit(1)

    if excel_file.split(".")[-1] != "xlsx":
        print("Expected a json file as first argument")
        print(USAGE)
        sys.exit(1)

    # ----------------------------------------
    #      Read config and data
    # ----------------------------------------
    config = configloader.load(config_file)
    for key, val in config[COLUMN_MAPPINGS_KEY].items():
        print(f"{key=}, {val=}")

    df = pd.read_excel(excel_file)
    print(df)

    # ----------------------------------------
    #      Clean data
    # ----------------------------------------
    df = cleaner.map_columns(df, config[COLUMN_MAPPINGS_KEY])
    print(f"Cleaned data: {df}")

    # ----------------------------------------
    #      Analyze data
    # ----------------------------------------
    sum = analyzer.sum_columns(df)
    print(sum)
