distancia = int(input("Qual a distância da sua viagem? "))
print("Você está prestes a começar uma viagem de {}Km".format(distancia))
if distancia <= 200:
    print("E o preço da sua passagem será de R${:.2f}".format(distancia*0.5))
else:
    print("E o preço da sua passagem será de R${:.2f}".format(distancia*0.45))