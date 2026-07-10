print ("Programa que você digita 1 número e ele te diz se é primo ou não")
c=0
numero = int(input("Digite o número: "))
for i in range (1,numero+1):
    if numero%i==0:
        c+=1
if c==2:
    print ("Esse número é primo")
else:
    print ("Esse número não é primo")   