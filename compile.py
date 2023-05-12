# from types_objet import *
from mot_clef import remplacer
from main import printf

def write_to_file(file:str, string:str):
    with open(file, "a", encoding='utf-8') as f:
        print(string, end=None, file=f)

def ligne(i : str) -> str:
    printf(f"Lecture :\n\"\"\"{i}\"\"\"\n")
    string = remplacer(i)
    return string

def compile(data:dict["files":list[str], "name":str]):
    printf("Compilation démarrée")
    printf(data)
    for file in data["files"]:
        printf(f"Fichier : {file}")
        try:
            with open(file, encoding='utf-8') as f:
                tmp = open(file[:-3] + ".py", "w", encoding='utf-8')
                print(f"\"\"\"Compilé par ...mais-c-est-un-langage-de-programmation de guigui0246\"\"\"\n\n", file=tmp)
                del(tmp)
                string = ""
                for i in f:
                    string += ligne(i)
                write_to_file(file[:-3] + ".py", string)
                printf(f"\"{string}\" écrit dans {file[:-3]}.py\n")
                del string
        except FileNotFoundError:
            printf(f"Fichier {file} non trouvé")
        except PermissionError:
            printf(f"Permissions manquantes pour {file} ou {file[:-3]}.py")
    with open(data["name"], "w", encoding='utf-8') as f:
        print(f"\"\"\"Compilé par ...mais-c-est-un-langage-de-programmation de guigui0246\"\"\"\n\n", file=f)
        for i in data["files"]:
            print(f"try:\n    from {i[:-3]} import main\nexcept ImportError:\n    pass\n", file=f)
        print("if __name__ == \"__main__\":\n    import sys\n    main(sys.argv)\n", file=f)
    printf("Compilation finie")
