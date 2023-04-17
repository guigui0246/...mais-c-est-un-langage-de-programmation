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

def get_info(argv:tuple[str]=sys.argv) -> dict["name":str, "files":list[str]]:
    data = {"name":"a.out", "files":["fic.fr", "f.fr"]}
    for file in data["files"]:
        if not file.endswith(".fr"):
            raise NameError(f"Le nom de fichier \"{file}\" est invalide (doit finir en .fr)")
    return data

if __name__ == "__main__":
    data = get_info()
    compile(data)
