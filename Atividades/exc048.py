print ("programa que calcula a soma entre todos os numeros impares que são mutiplos de 3 entre 1 e 500")
soma=0
for i in range (0, 501,):
    if i%3 == 0 and i %2 !=0 :
        soma+=i
print (f"A soma de todos os numeros impares,mutiplos de 3 é {soma}")