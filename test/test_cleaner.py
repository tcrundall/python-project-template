import pandas as pd
from cleaner import map_columns


def test_mappings_applied_successfully():
    # arrange
    mappings = {
        "orig-col-1": "mapped-col-1",
        "orig-col-2": "mapped-col-2",
        "orig-col-3": "mapped-col-2",
    }
    df = pd.DataFrame(
        {"orig-col-1": [1, 2], "orig-col-2": [1, 2], "orig-col-3": [1, 2]}
    )

    # act
    result = map_columns(df, mappings)
    result_columns = list(result.columns)

    # assert
    assert list(mappings.values()) == result_columns
    for orig_col in mappings.keys():
        assert orig_col not in result_columns
