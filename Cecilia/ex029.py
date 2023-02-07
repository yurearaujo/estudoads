velocidade = float(input("Informe a velocidade do carro: "))
if velocidade > 80:
    print("O carro será multado! Você excedeu o limite de velocidade que é de 80Km/h.")
    multa = 7*(velocidade-80)
    print("A multa será de {:.2f} reais.".format(multa))
print("Tenha um bom dia! Dirija com segurança!")








