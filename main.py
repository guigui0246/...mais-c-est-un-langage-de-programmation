import sys

if __name__ != "__main__":
    def printf(*args, **kwargs) -> None:
        print(*args, **kwargs, file=sys.stderr)
else:
    def printf(*args, **kwargs) -> None:
        print(*args, **kwargs)

from types import *

i = entier(3)
j = flottant(6)
k = i + j
k = entier(k)
j = flottant(i)
j += k
k = flottant(k)
j += k

printf(j)
