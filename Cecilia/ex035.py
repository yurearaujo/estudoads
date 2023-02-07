reta1 = float(input("Digite o primeiro comprimento: "))
reta2 = float(input("Digite o segundo comprimento: "))
reta3 = float(input("Digite o terceiro comprimento: "))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print("Essas medidas FORMAM um triângulo!")
else:
    print("NÃO é possível formar um triângulo!")
