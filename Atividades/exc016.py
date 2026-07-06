print ("Programa que tranforma um número real em inteiro")
from math import trunc
numero = float (input("Digite o numero real: "))
numeronovo = trunc(numero)
print (f"O número que era {numero} agora é {numeronovo}")