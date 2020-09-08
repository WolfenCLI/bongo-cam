from string import ascii_uppercase

import yaml


def get_tracked_keys() -> list:
    with open("./config.yml", "r+") as f:
        config: dict = yaml.safe_load(f)
        if not config['track_all_keys']:
            return config['tracked_keys']
        return ascii_uppercase
