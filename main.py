import sys

if __name__ != "__main__":
    def printf(*args, **kwargs) -> None:
        print("Compilateur:", *args, **kwargs, file=sys.stderr)
else:
    def printf(*args, **kwargs) -> None:
        print("Compilateur:", *args, **kwargs)

from types import *

def get_info(argv:tuple=sys.argv) -> dict:
    data = {"name":"a.out", "files":()}

def compile(data:dict):
    printf("Compilation démarrée")
    printf("Compilation finie")


if __name__ == "__main__":
    data = get_info()
    compile(data)
