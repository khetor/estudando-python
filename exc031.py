print ("Calculador preço da passagem por km (0.50 por km até 200km e 0.45 por km se for 200km+)")
kms = float (input("Digite a quantidade de kms da sua viagem: "))
if kms <=200:
    print (f"O preço da sua passagem é {kms*0.50}")
else:
    print (f"O preço da passagem é {kms*0.45}")