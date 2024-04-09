n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo número: "))
op = input("Qual operação desejada? \n -, +, * ou / \n")

if op == "/":
    print("Resultado:", n1/n2)
elif op == "+":
    print("Resultado:", n1+n2)
elif op == "-":
    print("Resultado:", n1-n2)
elif op == "*":
    print("Resultado:", n1*n2)
else:
    print("Operação incorreta.")
