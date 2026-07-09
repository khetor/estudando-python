print ("\033[35mJogue pedra papel e tesoura!: \033[m")
import random
import pygame
pygame.init()
jogadas = ["pedra","papel","tesoura"]
humanchoice = input("Digite sua jogada: ")
humanchoicelower = humanchoice.strip().lower()
if humanchoicelower != "pedra" and humanchoicelower != "papel" and humanchoicelower != "tesoura":
    print ("\033[31mIsso não faz parte do jogo,reinicie o programa.\033[m")
    exit ()
machinechoice = random.choice(jogadas)

if humanchoicelower == machinechoice:
    print (f"\033[33mVocê jogou {humanchoice} e o robô jogou {machinechoice},empate!\033[m")

elif humanchoicelower == "tesoura" and machinechoice == "papel":
    print ("\033[32mVocê jogou tesoura e o robô jogou papel,Você GANHOU!\033[m")
    pygame.mixer.music.load("correto-2.mp3")
    pygame.mixer.music.play()
elif humanchoicelower == "pedra" and machinechoice =="tesoura":
    print ("\033[32mVocê jogou pedra e o robô jogou tesoura,Você GANHOU!\033[m")
    pygame.mixer.music.load("correto-2.mp3")
    pygame.mixer.music.play()
elif humanchoicelower == "papel" and machinechoice =="pedra":
    print ("\033[32mVocê jogou papel e o robô jogou pedra,Você GANHOU!\033[m")
    pygame.mixer.music.load("correto-2.mp3")
    pygame.mixer.music.play()

elif humanchoicelower == "tesoura" and machinechoice == "pedra":
    print ("\033[31mVocê jogou tesoura e o robô jogou pedra,Você PERDEU!\033[m")
    pygame.mixer.music.load("bob-esponja-fail-sound.mp3")    
    pygame.mixer.music.play()    
elif humanchoicelower == "pedra" and machinechoice == "papel":
    print ("\033[31mVocê jogou pedra e o robô jogou papel,Você PERDEU!\033[m")
    pygame.mixer.music.load("bob-esponja-fail-sound.mp3")    
    pygame.mixer.music.play()    
elif humanchoicelower == "papel" and machinechoice == "tesoura":
    print ("\033[31mVocê jogou papel e o robô jogou tesoura,Você PERDEU!\033[m")
    pygame.mixer.music.load("bob-esponja-fail-sound.mp3")    
    pygame.mixer.music.play()  
input("Aperte Enter para sair.")
