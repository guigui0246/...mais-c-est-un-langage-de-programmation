class types(object):
    def entier(self, *args, **kwargs):
        return entier(*args, **kwargs)
    def flottant(self, *args, **kwargs):
        return flottant(*args, **kwargs)
    def texte(self, *args, **kwargs):
        return texte(*args, **kwargs)
    def liste(self, *args, **kwargs):
        return liste(*args, **kwargs)
    def liste_const(self, *args, **kwargs):
        return liste_const(*args, **kwargs)
    def dico(self, *args, **kwargs):
        return dico(*args, **kwargs)

class entier(int):
    def entier(self, *args, **kwargs):
        return entier(*args, **kwargs)

class flottant(float):
    def flottant(self, *args, **kwargs):
        return flottant(*args, **kwargs)

class texte(str):
    def texte(self, *args, **kwargs):
        return texte(*args, **kwargs)

class liste(list):
    def liste(self, *args, **kwargs):
        return liste(*args, **kwargs)

class liste_const(tuple):
    def liste_const(self, *args, **kwargs):
        return liste_const(*args, **kwargs)

class dico(dict):
    def dico(self, *args, **kwargs):
        return dico(*args, **kwargs)
