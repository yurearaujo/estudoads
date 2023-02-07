from random import randint
from time import sleep
computador = randint(0, 5)
chute = int(input("Chute um número: "))
print("PROCESSANDO...")
sleep(2)
if chute == computador:
    print("Parabéns você ganhou de mim!")
else:
    print("Você errou! eu pensei no número {} e não {}" .format(computador, chute))



