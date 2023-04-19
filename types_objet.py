##class types(object):
##    def entier(self, *args, **kwargs):
##        return entier(*args, **kwargs)
##    def flottant(self, *args, **kwargs):
##        return flottant(*args, **kwargs)
##    def texte(self, *args, **kwargs):
##        return texte(*args, **kwargs)
##    def liste(self, *args, **kwargs):
##        return liste(*args, **kwargs)
##    def liste_const(self, *args, **kwargs):
##        return liste_const(*args, **kwargs)
##    def dico(self, *args, **kwargs):
##        return dico(*args, **kwargs)
##    def complèxe(self, *args, **kwargs):
##        return complèxe(self, *args, **kwargs)
##    def types(self, *args, **kwargs):
##        return types(self, *args, **kwargs)
##    def groupe(self, *args, **kwargs):
##        return groupe(*args, **kwargs)
##    def groupe_const(self, *args, **kwargs):
##        return groupe_const(*args, **kwargs)
##    def octets(self, *args, **kwargs):
##        return octets(self, *args, **kwargs)
##    def liste_octets(self, *args, **kwargs):
##        return liste_octets(*args, **kwargs)
##
##
##class entier(int):
##    def entier(self, *args, **kwargs):
##        return entier(*args, **kwargs)
##
##class flottant(float):
##    def flottant(self, *args, **kwargs):
##        return flottant(*args, **kwargs)
##
##class texte(str):
##    def texte(self, *args, **kwargs):
##        return texte(*args, **kwargs)
##
##class liste(list):
##    def liste(self, *args, **kwargs):
##        return liste(*args, **kwargs)
##
##class liste_const(tuple):
##    def liste_const(self, *args, **kwargs):
##        return liste_const(*args, **kwargs)
##
##class dico(dict):
##    def dico(self, *args, **kwargs):
##        return dico(*args, **kwargs)
##
##class complèxe(complex):
##    def complèxe(self, *args, **kwargs):
##        return complèxe(self, *args, **kwargs)
##
##class groupe(set):
##    def groupe(self, *args, **kwargs):
##        return groupe(*args, **kwargs)
##
##class groupe_const(frozenset):
##    def groupe_const(self, *args, **kwargs):
##        return groupe_const(*args, **kwargs)
##
##class octets(bytes):
##    def octets(self, *args, **kwargs):
##        return octets(self, *args, **kwargs)
##
##class liste_octets(bytearray):
##    def liste_octets(self, *args, **kwargs):
##        return liste_octets(*args, **kwargs)


try:
    from mot_clef import replace
    def add_types(liste_replace:list[replace]) -> list[replace]:
        liste_replace.append(replace("str", "texte"))
        liste_replace.append(replace("int", "entier"))
        liste_replace.append(replace("float", "flottant"))
        liste_replace.append(replace("complex", "complèxe"))
        liste_replace.append(replace("list", "liste"))
        liste_replace.append(replace("tuple", "liste_const"))
        liste_replace.append(replace("range", "liste_continue"))
        liste_replace.append(replace("dict", "dico"))
        liste_replace.append(replace("set", "groupe"))
        liste_replace.append(replace("frozenset", "groupe_const"))
        liste_replace.append(replace("bool", "booléen"))
        liste_replace.append(replace("bytes", "octets"))
        liste_replace.append(replace("bytearray", "liste_octet"))
        liste_replace.append(replace("memoryview", "vue_mémoire"))
        return liste_replace
except ModuleNotFoundError:
    def add_types(liste_replace:list) -> list:
        import sys
        print("Types non chargés", file=sys.stderr)
        return liste_replace
