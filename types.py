class types(object):
    def entier(self, *args, **kwargs):
        return entier(*args, **kwargs)
    def flottant(self, *args, **kwargs):
        return flottant(*args, **kwargs)

class entier(int):
    def entier(self, *args, **kwargs):
        return entier(*args, **kwargs)

class flottant(float):
    def flottant(self, *args, **kwargs):
        return flottant(*args, **kwargs)
