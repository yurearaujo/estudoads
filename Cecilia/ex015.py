km = float(input("Quantos km foram percorridos? "))
d = int(input("Por quantos dias o carro foi alugado? "))
print("Você percorreu {}km durante {} dias." .format(km, d))
print("O valor total a ser pago é de R${:.2f}." .format((60 * d) + (0.15 * km)))
