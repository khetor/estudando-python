print ("Programa que lê um número de 0 a 9999")

numero = input("Digite o número:")

print (f"A milhar é {numero[-4:-3]}")
print (f"A centena é {numero[-3:-2]}")
print (f"A dezena é {numero[-2:-1]}")
print (f"A unidade é {numero[-1:]}")