import tomllib

def read_toml(filename):
    with open(filename, 'rb') as f:
        return tomllib.load(f)