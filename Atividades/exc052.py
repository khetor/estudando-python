print ("Programa que diz se um número é primo ou não.")
contador = 0
numero = int(input("Digite o número: "))
for i in range(1,numero+1):
    if numero%i==0:
        contador+=1
if contador ==2:
    print("Seu número é primo!")
else:
    print ("Seu número não é primo!")