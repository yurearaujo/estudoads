salario = float(input("Qual é o salário do funcionário? R$"))
if salario <= 1250:
    print("Quem ganhava {} reais passa a ganhar {} reais agora.".format(salario, salario * 0.15 + salario))
else:
    print("Quem ganhava {} reais passa a ganhar {} reais agora.".format(salario, salario * 0.10 + salario))
