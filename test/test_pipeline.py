import pandas as pd

from mydatapipeline.pipeline import run


def test_column_renamings():
    # arrange
    config_file = "test/resources/config.json"
    excel_file = "test/resources/example-sheet.xlsx"
    expected_result = pd.Series({"price": 36, "cost-val": 393}, dtype=int)

    # act
    result = run(config_file, excel_file)

    # assert
    assert all(expected_result == result)
