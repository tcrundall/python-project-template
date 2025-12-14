import configloader


def test_load_config():
    # arrange
    config_file = "test/resources/config.json"
    expected_config = {
        "some-key": "some-val",
        "column-mappings": {"price-val": "price", "time of day ": "time"},
    }

    # act
    config = configloader.load(config_file)

    # assert
    assert expected_config == config
