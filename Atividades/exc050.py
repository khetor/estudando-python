print ("Programa que lê SOMENTE números pares e soma eles.(Pode digitar impares pra testar" \
"e serão DESCONSIDERADOS!)")
soma=0
for i in range (1, 7):
    valor = int(input("Digite um número inteiro: "))
    if valor %2 == 0:
        soma+=valor
        print ()
    else:
        print ("(Número desconsiderado)")
print (f"A soma dos números pares é {soma}")