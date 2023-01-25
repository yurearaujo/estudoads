#co = float(input("Informe o comprimento do cateto oposto: "))
#ca = float(input("Informe o comprimento do cateto adjacente: "))
#h = (co ** 2) + (ca ** 2)
#print("A Hipotenusa deste triângulo mede {:.2f}".format(h ** (1/2)))

from math import hypot
co = float(input("Informe o comprimento do cateto oposto: "))
ca = float(input("Informe o comprimento do cateto adjacente: "))
h = hypot(co, ca)
print("A Hipotenusa é igual a {:.2f}".format(h))
