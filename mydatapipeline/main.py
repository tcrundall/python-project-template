import sys

from mydatapipeline.pipeline import run

USAGE = """
        Usage: python main.py my-config-file.json my-data.xlsx
        """

COLUMN_MAPPINGS_KEY = "column-mappings"


def main():
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
        print("Expected an xlsx file as first argument")
        print(USAGE)
        sys.exit(1)

    run(config_file, excel_file)


if __name__ == "__main__":
    main()
