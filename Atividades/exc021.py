print ("Programa que toca som:")
import pygame

pygame.init()
pygame.mixer.music.load("rizz-sound-effect.mp3")
pygame.mixer.music.play()
input ("Aperte enter para finalizar.")