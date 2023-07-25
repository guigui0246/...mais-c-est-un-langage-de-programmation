exceptions = [".git"]

try:
    from mot_clef import replace
    def add_custom(liste_replace:list[replace]) -> list[replace]:
        filelist = []
        try:
            import os
            paths = [os.getcwd()]
            while not len(paths) == 0:
                actual_path = paths.pop()
                print(actual_path)
                filelist = filelist + [os.path.join(actual_path, f) for f in os.listdir(actual_path) if os.path.isfile(os.path.join(actual_path, f)) and f.endswith(".reg")]
                paths = paths + [os.path.join(actual_path, f) for f in os.listdir(actual_path) if f not in exceptions and not os.path.isfile(os.path.join(actual_path, f))]
        except:
            filelist = []
        for path in filelist:
            with open(path) as file:
                f = file.readlines()
            for i in f:
                e = i.split()
                for j in range(len(e)):
                    if e[j] == "":
                        e.remove("")
                        j -= 1
                if len(e) == 2:
                    liste_replace.append(replace(e[0], e[1]))
                else:
                    import sys
                    print(f"La ligne \"{i}\" est invalide est n'a donc pas été chargée", file = sys.stderr)
        if len(liste_replace) < 1:
            import sys
            print("Aucune fonction customisée trouvée", file=sys.stderr)
        return liste_replace
except ModuleNotFoundError:
    def add_custom(liste_replace:list) -> list:
        import sys
        print("Fonctions custommisées non chargées", file=sys.stderr)
        return liste_replace
