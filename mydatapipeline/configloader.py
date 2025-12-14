import json


def load(config_file):
    with open(config_file) as fp:
        config = json.load(fp)
    print(config)
    return config
