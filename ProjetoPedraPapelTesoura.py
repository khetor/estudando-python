print ("Bem vindo ao Pedra papel e tesoura!,Se divirta!")
import random
humanchoice = input("Digite sua jogada!: ")

humanchoicelow = humanchoice.strip().lower()

tesoura = ("tesoura")
papel = ("papel")
pedra = ("pedra")

machine_lista = [tesoura,papel,pedra]

if humanchoicelow != machine_lista[0] and humanchoicelow != machine_lista[1] and humanchoicelow != machine_lista[2]:
    print("Ei isso não faz parte das escolhas,joga direito ai pow!")
    exit()

machinechoice = random.choice(machine_lista)

print (f"Você escolheu {humanchoice} e o computador escolheu {machinechoice}")

if humanchoicelow==machinechoice:
    print (f"Você escolheu {humanchoicelow} e ele támbem,empate.")


if humanchoicelow == machine_lista[0] and machinechoice == machine_lista [1]:
    print ("Você escolheu tesoura e o robo papel KKKKKKK ganhasse")

if humanchoicelow ==machine_lista[1] and machinechoice == machine_lista[2]:
    print ("Você escolheu papel e o robo pedra KKKKKKK ganhasse")

if humanchoicelow ==machine_lista[2] and machinechoice ==machine_lista[0]:
    print ("Você escolheu pedra e o robo tesoura KKKKKKK ganhasse")


if humanchoicelow == machine_lista[0] and machinechoice == machine_lista[2]:
    print ("Perdesse newbaa,escolhece tesoura e ele pedra")

if humanchoicelow ==machine_lista[1] and machinechoice == machine_lista[0]:
    print ("Perdesse newbaa,escolhece papel e ele tesoura")

if humanchoicelow ==machine_lista[2] and machinechoice ==machine_lista[1]:
    print("Perdesse newbaa,escolhece pedra e ele papel")