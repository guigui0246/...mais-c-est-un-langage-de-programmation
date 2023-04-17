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
    def complèxe(self, *args, **kwargs):
        return complèxe(self, *args, **kwargs)
    def types(self, *args, **kwargs):
        return types(self, *args, **kwargs)
    def groupe(self, *args, **kwargs):
        return groupe(*args, **kwargs)
    def groupe_const(self, *args, **kwargs):
        return groupe_const(*args, **kwargs)
    def octets(self, *args, **kwargs):
        return octets(self, *args, **kwargs)
    def liste_octets(self, *args, **kwargs):
        return liste_octets(*args, **kwargs)


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

class complèxe(complex):
    def complèxe(self, *args, **kwargs):
        return complèxe(self, *args, **kwargs)

class groupe(set):
    def groupe(self, *args, **kwargs):
        return groupe(*args, **kwargs)

class groupe_const(frozenset):
    def groupe_const(self, *args, **kwargs):
        return groupe_const(*args, **kwargs)

class octets(bytes):
    def octets(self, *args, **kwargs):
        return octets(self, *args, **kwargs)

class liste_octets(bytearray):
    def liste_octets(self, *args, **kwargs):
        return liste_octets(*args, **kwargs)
