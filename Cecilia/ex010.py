d1 = float(input("Quantos reais você tem? R$ "))
d2 = d1 / 3.27
d3 = d1 / 5.57
print("Com R${:.2f} você pode comprar US${:.2f} ou €{:.2f}.".format(d1, d2, d3))
