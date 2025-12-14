import pandas as pd

from mydatapipeline import (
    analyzer,
    cleaner,
    configloader,
)

USAGE = """
        Usage: python main.py my-config-file.json my-data.xlsx
        """

COLUMN_MAPPINGS_KEY = "column-mappings"


def run(config_file, excel_file):
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

    return sum
