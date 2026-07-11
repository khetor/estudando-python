print ("Programa que calula a soma de todos os números impares e multiplos de 3 entre 1 e 500")
soma=0
for i in range (1,501):
    if i %3==0 and i%2!=0:
        soma+=i
print(soma)