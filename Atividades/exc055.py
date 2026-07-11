print ("Programa que lê o peso de 5 pessoas e diz qual a mais pesada e menos pesada.")
maior = float(input("Digite um peso por vez: "))
menor = maior
for i in range(2,6):
    peso = float(input("Digite um peso por vez: "))
    if peso>maior:
        maior=peso
    elif peso<menor:
        menor=peso
print (f"O mais pesado tem {maior}KG")
print (f"O mais leve tem {menor}KG") 