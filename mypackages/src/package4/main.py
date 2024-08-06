
from package1 import hello1
from package2 import hello2
from package4.submodule4 import submodule4

def main():
    print(hello1())
    print(hello2())
    print(submodule4())

if __name__=="__main__":
    main()