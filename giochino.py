import pygame
import sys


pygame.init()


screen=pygame.display.set_mode((800, 600))

pygame.display.set_caption('giochino')

immagine=pygame.image.load('personaggio.jpg')
immagine=pygame.transform.scale(immagine, (100, 52))
immagine=pygame.transform.flip(immagine, True, False)
immaginex=10
immaginey=599
sfondo=pygame.image.load('sfondo.png')



clock=pygame.time.Clock()

FPS=60

def disegna():

    screen.blit(sfondo, (0, 0))

    screen.blit(immagine, (immaginex, immaginey))

def aggiorna():

    pygame.display.update()

    pygame.time.Clock().tick(FPS)

while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.quit()

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                immaginex

