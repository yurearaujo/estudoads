import math
c1 = float(input("Informe o valor do primeiro cateto: "))
c2 = float(input("Informe o valor do segundo cateto: "))
h = math.sqrt((c1 ** 2) + (c2 ** 2))
print("A hipotenusa é igual a {:.2f}".format(h))

from math import hypot
co = float(input("Informe o valor do primeiro cateto: "))
ca = float(input("Informe o valor do segundo cateto: "))
h = hypot(co, ca)
print("O valor da hipotenusa é {:.2f}" .format(h))
