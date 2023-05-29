import pygame, sys
from pygame.locals import *

larghezza_schermo = 800
altezza_schermo = 600
screen = pygame.display.set_mode((larghezza_schermo, altezza_schermo))
pygame.display.set_caption("Labirinto per gioco informatica")
immagine_avvio = pygame.image.load("colosseo.png")
immagine_avvio = pygame.transform.scale(immagine_avvio, (800, 600))
screen.blit(immagine_avvio, (0, 0))

class Miascritta:
    def __init__(self, frase, pos, font, sizefont, colore) -> None:
        self.frase=frase
        self.pos=pos
        self.font=font
        self.sizefont=sizefont
        self.colore=colore
    
    def draw(self, bold, underline, italic):
        fnt=pygame.font.SysFont(self.font, self.sizefont)
        fnt.set_bold(bold)
        fnt.set_underline(underline)
        fnt.set_italic(italic)
        surf=fnt.render(self.frase, True, self.colore)
        screen.blit(surf, self.pos)


f=Miascritta("il labiribto dl RE di roma",(200, 50),"Arial", 32, "green" )
f.draw(True, False, False)



pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()