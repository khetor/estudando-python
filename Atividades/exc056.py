print ("Programa que lê o nome,idade,sexo de 4 pessoas e dps mostra:")
print ("A média de idade de todos.")
print ("Qual o nome do homem mais velho.")
print ("Quantas mulheres tem menos de 20 anos.")
contadoridade=0
contadormulheres=0


primeironome = input("Digite um nome: ")
maioridade = int(input("Digite a idade: "))
sexo = input("Digite o sexo(M/F): ")
sexoupper = sexo.upper()
contadoridade += maioridade
if maioridade<20 and sexoupper == "F":
    contadormulheres+=1


for perguntas in range(1,4):
    nome = input("Digite um nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo(M/F): ")
    sexoupper = sexo.upper()
    contadoridade += idade
    if idade<20 and sexoupper == "F":
        contadormulheres+=1
    if maioridade<idade and sexoupper =="M":
        maioridade=idade
        primeironome=nome

media = contadoridade/4
print (f"A média de idade das pessoas do grupo é {media:.2f}")
print (f"O nome do homem mais velho é {primeironome}.")
print (f"Temos {contadormulheres} mulher com menos de 20 anos.")
