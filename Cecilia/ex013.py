s = float(input("Digite o valor do salário: "))
ns = s + (s * 15/100)
print("O seu salário era de R${:.2f} com o aumento de 15% o seu novo salário passa a ser R${:.2f}" .format(s, ns))
