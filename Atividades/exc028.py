print ("Programa que escolhe um número entre 0 e 5 e o jogador tem que acertar")
import random
nrandom = random.randint(0,5)
nresposta = int (input("Digite o número de 0 a 5: "))
if nresposta >5:
    print ("EI ESSE NÚMERO NAO TA NO JOGO,RECOMEÇE O PROGRAMA!")
    exit()
if nresposta ==nrandom:
    print (f"Você acertou!({nrandom})")
else:
    print (f"Você errou kkkk era {nrandom} e não {nresposta}")