
from package1 import hello1
from package2 import hello2
from package4.submodule4 import submodule4
from utils import read_toml

def main():
    print(hello1())
    print(hello2())
    print(submodule4())

    pyproject = read_toml('pyproject.toml')
    for dep in pyproject['tool']['poetry']['dependencies']:
        print(dep)

    # for dep in pyproject['tool']['poetry']['group']['dev']['dependencies']:
    #     print(dep)
    

if __name__=="__main__":
    main()