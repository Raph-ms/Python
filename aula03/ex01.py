num = int(input("digite um numero com três digitos"))
d1 = num // 100
d2 = num % 100 // 10
d3 = num % 10
inverso = d3*100+d2*10+d1
print("O inverso do nu mero digitado é", inverso)