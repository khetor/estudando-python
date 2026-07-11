print ("Programa que lê o ano de nascimento de sete pessoas e no final mostra quantas são" \
"maiores de idade e quantas não são (21 anos)")
menor=0
maior=0
for i in range(1,8):
    anos = int(input("Digite o de nascimento de cada pessoa: "))
    idade=2026-anos
    if idade >=21:
      maior+=1
    else:
        menor+=1
print(f"{maior} tem mais de 21 anos!")
print (f"{menor} tem menos de 21 anos!")