from math import sin, cos, tan, radians
ang = float(input("Digite um ângulo: "))
seno = sin(radians(ang))
print("O Seno de {} é {:.2f}".format(ang, seno))
cosseno = cos(radians(ang))
print("O Cosseno de {} é {:.2f}".format(ang, cosseno))
tangente = tan(radians(ang))
print("A Tangente de {} é {:.2f}".format(ang, tangente))

