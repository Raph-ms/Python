idade = int(input("Digite sua idade:"))

if idade < 16:
    print("Não eleitor.")
elif idade >=18 and idade < 66:
    print("Eleitor obrigatório.")
else:
    print("Eleitor facultativo.")