velocidade = int(input("Qual a velocidade atual do seu carro? "))
if velocidade < 80:
    print("Tenha um bom dia! continue dirigindo em segurança!")
else:
    print("""MULTADO! você excedeu o limite permitido de 80km/h 
    você deve pagar uma multa de R${}""".format((velocidade - 80) * 7))