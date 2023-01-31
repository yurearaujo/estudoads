from random import choice
a1 = str(input("Escreva o nome do primeiro aluno: "))
a2 = str(input("Escreva o nome do segundo aluno: "))
a3 = str(input("Escreva o nome do terceiro aluno: "))
a4 = str(input("Escreva o nome do quarto aluno: "))
lista = [a1, a2, a2, a3, a4]
sorteado = choice(lista)
print("O aluno escolhido foi {}".format(sorteado))



