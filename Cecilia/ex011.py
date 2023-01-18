l = float(input("Digite a largura da parede: "))
a = float(input("Digite a altura da parede: "))
area = l*a
print("A área da sua parede é de {}m²." .format(area))
tinta = area / 2
print("Para pintar {}m² você precisará de {}l de tinta." .format(area, tinta))
