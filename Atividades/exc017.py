print ("Programa que calcula a hipotenusa:")
from math import sqrt,pow
cateto1 = float (input("Qual o valor do primeiro cateto?: "))
cateto2 = float (input("Qual o valor do segundo cateto?: "))
soma = (pow(cateto1,2) + pow(cateto2,2)) 
hipotenusa = sqrt(soma)
print (f"A soma dos quadrados {cateto1} e {cateto2} dão a hipotenusa {hipotenusa:.3f}")