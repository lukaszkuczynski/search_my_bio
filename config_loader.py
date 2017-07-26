import yaml

def load_config(path):
    with (open(path)) as f:
        config = yaml.load(f)
        return config