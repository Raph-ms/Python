a = float(input("Digite o valor de de A:"))
b = float(input("Digite o valor de de B:"))
c = float(input("Digite o valor de de C:"))

delta = b**2 -4 * a * c

if a == 0:
    print("Não é equação de segundo grau.")
elif delta >=0:
    raiz1 = (- b + delta**0.5) / (2 * a)
    raiz2 = (- b - delta**0.5) / (2 * a)
    print("O valor da primeira raiz é:", raiz1, "o valor da segunda raiz é:",raiz2) 
else:
    print("Não há raízes reais")
  