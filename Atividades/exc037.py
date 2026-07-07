print ("Digite um número para escolher se quer converter para binario,octal ou hexadecimal.")
numero = int(input("Digite o número: "))
escolha = input("Digite '1' para Bin,'2' para oct, '3' para hexa: ")
if escolha == "1":
    print (bin(numero))
elif escolha == "2":
    print (oct(numero))
elif escolha == "3":
    print (hex(numero))
else:
    print ("\033[31mOpcão invalida!\033[m")