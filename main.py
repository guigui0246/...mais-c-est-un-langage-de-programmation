import sys

if __name__ != "__main__":
    def printf(*args, **kwargs) -> None:
        print("Compilateur:", *args, **kwargs, file=sys.stderr)
else:
    def printf(*args, **kwargs) -> None:
        print("Compilateur:", *args, **kwargs)

try:
    from compile import compile
except ImportError:
    pass

def get_info(argv:tuple=sys.argv) -> dict:
    data = {"name":"a.out", "files":["fic.fr"]}
    for file in data["files"]:
        if not file.endswith(".fr"):
            raise NameError(f"Le nom de fichier \"{file}\" est invalide (doit finir en .fr)")
    return data

if __name__ == "__main__":
    data = get_info()
    compile(data)
