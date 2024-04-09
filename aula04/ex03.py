produto = input("Qual o nome do produto?")
valor = float(input("Qual o valor do produto?"))

if valor < 10:
    print("O valor de venda do", produto,"é: R$", valor*0.70 + valor)
elif valor >= 10 and valor < 30:
    print("O valor de venda do", produto,"é: R$", valor*0.50 + valor)
elif valor >= 30 and valor <50:
    print("O valor de venda do", produto,"é: R$", valor*0.40 + valor)
else:
    print("O valor de venda do",produto,"é: R$", valor*0.30 + valor)