import tomllib

def read_toml(filename):
    with open(filename, 'rb') as f:
        pyproject = tomllib.load(f)
    return pyproject

    # for dep in pyproject['tool']['poetry']['group']['dev']['dependencies']:
    #     print(dep)
    
    # for dep in pyproject['tool']['poetry']['dependencies']:
    #     print(dep)