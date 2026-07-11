import time
import pygame
pygame.init()
print ("Contagem Regressiva de 10 a 0.")
input ("Aperte enter para começar a contagem: ")
for contagem in range (10, 0, -1):
    print(contagem)
    pygame.mixer.music.load("bipp.mp3")
    pygame.mixer.music.play()
    time.sleep(1)
print("ACABOUU")
pygame.mixer.music.load("fogos.mp3")
pygame.mixer.music.play()
input ("Aperte enter para finalizar o programa: ")
