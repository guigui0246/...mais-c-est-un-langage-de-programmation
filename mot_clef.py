class replace():
    def __init__(self, str1:str, str2:str) -> None:
        self.str1 = str1
        self.str2 = str2

    def __call__(self, string:str) -> str:
        if string == self.str1:
            return self.str2
        if string == self.str2:
            return self.str1
        return ""

liste_replace = []

try:
    from types import add_types
    liste_replace = add_types(liste_replace)
except ModuleNotFoundError:
    import sys
    print("Types non chargés", file=sys.stderr)
except ImportError:
    pass

try:
    from error import add_errors
    liste_replace = add_errors(liste_replace)
except ModuleNotFoundError:
    import sys
    print("Erreurs non chargées", file=sys.stderr)
except ImportError:
    pass

def add_keywords(liste_replace:list[replace]) -> list[replace]:
    liste_replace.append(replace("None", "Vide"))
    liste_replace.append(replace("False", "Faux"))
    liste_replace.append(replace("True", "Vrai"))
    liste_replace.append(replace("and", "et"))
    liste_replace.append(replace("as", "comme"))
    liste_replace.append(replace("assert", "vérifier"))
    liste_replace.append(replace("async", "asynchroniser"))
    liste_replace.append(replace("await", "attendre"))
    liste_replace.append(replace("break", "casser_boucle"))
    liste_replace.append(replace("class", "classe"))
    liste_replace.append(replace("continue", "prochaine_itération"))
    liste_replace.append(replace("def", "définir"))
    liste_replace.append(replace("del", "supprimer"))
    liste_replace.append(replace("elif", "et_si"))
    liste_replace.append(replace("else", "sinon"))
    liste_replace.append(replace("except", "rattraper"))
    liste_replace.append(replace("finally", "finalement"))
    liste_replace.append(replace("for", "pour"))
    liste_replace.append(replace("from", "depuis"))
    liste_replace.append(replace("global", "globale"))
    liste_replace.append(replace("if", "si"))
    liste_replace.append(replace("import", "importer"))
    liste_replace.append(replace("in", "dans"))
    liste_replace.append(replace("is", "est"))
    liste_replace.append(replace("lambda", "lambda"))
    liste_replace.append(replace("nonlocal", "non_locale"))
    liste_replace.append(replace("not", "non"))
    liste_replace.append(replace("or", "ou"))
    liste_replace.append(replace("pass", "passer"))
    liste_replace.append(replace("raise", "remonter"))
    liste_replace.append(replace("return", "renvoyer"))
    liste_replace.append(replace("try", "essayer"))
    liste_replace.append(replace("while", "tant_que"))
    liste_replace.append(replace("with", "avec"))
    liste_replace.append(replace("yield", "renvoyer_générateur"))
    return liste_replace

liste_replace = add_keywords(liste_replace)

def remplacer(string:str) -> str | None:
    global liste_replace
    liste = [i(string) for i in liste_replace]
    string = ""
    for i in liste:
        string += i
    if string == "":
        return None
    return string
