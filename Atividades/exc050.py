print ("Programa que lê seis números inteiros e soma somente os pares")
soma=0
for i in range(1, 7):
    numeros = int(input("Digite um número: "))
    if numeros%2==0:
        soma+=numeros
    else:
        print("Número ignorado na conta.")
print (F"A soma dos números pares é {soma}")