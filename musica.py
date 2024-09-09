import pygame
from pygame import mixer
import pygame.mixer_music

def tocar_musica():
    if not pygame.mixer.music.get_busy():  # Verifica se a música já está tocando
        mixer.music.load('audios\menu.wav')
        mixer.music.play(-1)