print ("Program que calcula uma Progressão aritimetrica.")
primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
for i in range(0, 10):
    termos=primeiro_termo+razao*i
    print (termos)