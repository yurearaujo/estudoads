preço = float(input("Qual o valor do produto que você quer aplicar o desconto? "))
desc = preço - preço * (5 / 100)
print("O valor deste produto após o desconto é de {} reais".format(desc))
