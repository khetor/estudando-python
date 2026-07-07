print ("Programa para mostrar a categoria dos competidores de natação segundo o CNN(orgão inventado)")
ano = int(input("Digite o ano de nascimento do atelta: "))
idade = 2026-ano
if idade <=9:
    print (f"Você tem {idade} anos e está na categoria MIRIM")
elif idade <=14:
    print (f"Você tem {idade} anos e está na categoria INFANTIL")
elif idade <=19:
    print (f"Você tem {idade} anos e está na categoria JUNIOR")
elif idade <=20:
    print (f"Você tem {idade} anos e está na categoria SENIOR")
else:
    print (f"Você tem {idade} anos e está na categoria MASTER")