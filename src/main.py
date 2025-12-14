import sys
import json
import pandas as pd

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
    with open(config_file) as fp:
        config = json.load(fp)
    print(config)
    for key, val in config[COLUMN_MAPPINGS_KEY].items():
        print(f"{key=}, {val=}")

    df = pd.read_excel(excel_file)
    print(df)

    # ----------------------------------------
    #      Clean data
    # ----------------------------------------
    df = df.rename(columns=config[COLUMN_MAPPINGS_KEY])
    print(f"Cleaned data: {df}")

    # ----------------------------------------
    #      Analyze data
    # ----------------------------------------
    sum = df.sum(numeric_only=True)
    print(sum)
