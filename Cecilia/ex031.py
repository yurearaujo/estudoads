distancia = float(input("Informe a distância da viagem: "))
if distancia <= 200:
    print("A sua viagem tem {}Km." .format(distancia))
    preco = distancia * 0.50
else:
    print("A sua viagem tem {}Km.".format(distancia))
    preco = 0.45 * distancia
print("A sua viagem custará R${:.2f}." .format(preco))
