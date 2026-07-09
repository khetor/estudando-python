import time
import pygame
pygame.init()
print ("CONTAGEM REGREESIVA DE 10 SEGUNDOS QUANDO VOCÊ APERTAR ENTER!")
input (":")
for i in range (10, 0, -1):
    print(i)
    time.sleep(1)
    pygame.mixer.music.load("bipp.mp3")
    pygame.mixer.music.play()
pygame.mixer.music.load("fogos.mp3")
pygame.mixer.music.play()
input("Encerre o programa apertando enter: ")

