from random import randint
from time import sleep
print("-=-" * 30)
numero = int(input("Vou pensar em um número entre zero e cinco. Tente adivinhar: "))
print("-=-" * 30)
sorteio = randint(0, 5)
print("PROCESSANDO")
sleep(2)
if sorteio == numero:
    print("Parabéns, você conseguiu me vencer!")
else:
    print("Você errou! eu pensei no número {}, e não no {}".format(sorteio, numero))