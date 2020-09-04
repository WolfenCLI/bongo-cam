import yaml


def get_tracked_keys() -> list:
    with open("./config.yml", "r+") as f:
        return yaml.safe_load(f)['tracked_keys']
