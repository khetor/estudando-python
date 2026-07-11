print ("Programa que verifica se a frase é um palindromo.")
frase = input("Digite a frase: ")
frasetratada = frase.upper().strip().replace(" ","")
contrario = frasetratada[::-1]
if contrario==frasetratada:
    print (f"{frasetratada} é igual à {contrario}. É um palindromo.")
else:    
    print (f"{frasetratada} não é igual à {contrario}. Não é um palindromo.")