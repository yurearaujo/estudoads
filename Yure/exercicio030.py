numero = int(input("Digite um número: "))
divisao = numero % 2
if divisao == 0:
    print("O número {} é par".format(numero))
else:
    print("O número {} é ímpar".format(numero))