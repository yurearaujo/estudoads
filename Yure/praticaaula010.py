n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print("A sua média foi de {:.1f}".format(m))
if m >= 7:
    print("Parabéns, você foi aprovado!")
else:
    print("Sinto muito, você não conseguiu a aprovação...")
