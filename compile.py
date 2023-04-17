# from types_objet import *
from mot_clef import remplacer
from main import printf

def write_to_file(file:str, string:str):
    with open(file, "a") as f:
        print(string, end=None, file=f)

def ligne(i : str) -> str:
    printf(f"Lecture :\n\"\"\"{i}\"\"\"\n")
    string = ""
    l = i.split(sep=" ")
    for j in l:
        tmp = remplacer(j)
        if (tmp == None):
            string += j
        else:
            string += tmp
        del tmp
        if (j != l[len(l) - 1]):
            string += " "
    del l
    return string

def compile(data:dict["files":list[str], "name":str]):
    printf("Compilation démarrée")
    printf(data)
    for file in data["files"]:
        printf(f"Fichier : {file}")
        with open(file) as f:
            tmp = open(file[:-3] + ".py", "w")
            del(tmp)
            string = ""
            for i in f:
                string += ligne(i)
            write_to_file(file[:-3] + ".py", string)
            printf(f"\"{string}\" écrit dans {file[:-3]}.py\n")
            del string
    printf("Compilation finie")