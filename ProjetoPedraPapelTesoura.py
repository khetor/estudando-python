print ("Bem vindo ao Pedra papel e tesoura!,Se divirta!")
import random
humanchoice = input("Digite sua jogada!: ")

humanchoicelow = humanchoice.strip().lower()

machine_lista = ["tesoura","papel","pedra"]

if humanchoicelow != machine_lista[0] and humanchoicelow != machine_lista[1] and humanchoicelow != machine_lista[2]:
    print("Ei isso não faz parte das escolhas,joga direito ai pow!")
    exit()

machinechoice = random.choice(machine_lista)

if humanchoicelow==machinechoice:
    print (f"Você escolheu {humanchoicelow} e ele támbem,empate.")

if humanchoicelow == "tesoura" and machinechoice == "papel":
    print ("Você escolheu tesoura e o robo papel KKKKKKK ganhasse")

if humanchoicelow =="papel" and machinechoice == "pedra":
    print ("Você escolheu papel e o robo pedra KKKKKKK ganhasse")

if humanchoicelow =="pedra" and machinechoice =="tesoura":
    print ("Você escolheu pedra e o robo tesoura KKKKKKK ganhasse")


if humanchoicelow == "tesoura" and machinechoice == "pedra":
    print ("Perdesse newbaa,escolhece tesoura e ele pedra")

if humanchoicelow =="papel" and machinechoice == "tesoura":
    print ("Perdesse newbaa,escolhece papel e ele tesoura")

if humanchoicelow =="pedra" and machinechoice =="papel":
    print("Perdesse newbaa,escolhece pedra e ele papel")