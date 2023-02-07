x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))
maior = x
if y>x and y>z:
    maior = y
if z>x and z>y:
    maior = z
print("O maior valor é {}." .format(maior))
menor = y
if x<z and x<y:
    menor = x
if z<x and z<y:
    menor = z
print("O menor valor é {}." .format(menor))








