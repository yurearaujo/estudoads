nome = input("Digite o seu nome completo: ").strip()
print("Analisando seu nome...")
print("Em letras maiúsculas é {}" .format(nome.upper()))
print("Em letras minúscula é {}" .format(nome.lower()))
print("Seu nome completo possui {} letras" .format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras" .format(nome.find(" ")))








