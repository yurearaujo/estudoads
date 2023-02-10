s = float(input("Qual o salário atual? "))
if s >= 1250:
   a = s + (s * 10/100)
else:
   a = s + (s * 15/100)
print("O salário atual é R${:.2f} ,com o aumento o novo salário é R${:.2f}." .format(s, a))
