import pygame, sys

from pygame.locals import *


pygame.init()

#qua ci mettiamo le dimensione dello schermo 
WIDTH = 800
HEIGHT = 600


WHITE = (255, 255, 255)
RED = (255, 0, 0)
gioco_attivo = False
tempo_inizio = 0
punteggio = 0



# Creazione della finestra di gioco
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labirinto per gioco informatica")

# Dimensioni del quadrato
square_size = 40

# Posizione iniziale del quadrato
quadrato_x = square_size
quadrato_y = square_size
class Player(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.image_player = pygame.image.load("labirinto/barba.jpeg")
        self.rect_player = self.image.get.rect(center = (20,20))
        self.self.square_size = 40
        self.quadrato_y = 40
        self.quadrato_x = 40



player = pygame.sprite.GroupSingle()
player.add(Player())

#qui creiamo il labirinto iniziale, poi ci lavoraiamo ingrandendolo
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#qua con le matrici disegnaimo il labirninto
def lab():
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            if labirinto[i][j] == 1:
                pygame.draw.rect(screen, WHITE, (j * square_size, i * square_size, square_size, square_size))

# Ciclo fondamentale, qui possiamo anche usare w,a,s,d al posto delle frecce
while True:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if labirinto[int(quadrato_y / square_size) - 1][int(quadrato_x / square_size)] == 0:
                    quadrato_y -= square_size
            elif event.key == pygame.K_DOWN:
                if labirinto[int(quadrato_y / square_size) + 1][int(quadrato_x / square_size)] == 0:
                    quadrato_y += square_size
            elif event.key == pygame.K_LEFT:
                if labirinto[int(quadrato_y / square_size)][int(quadrato_x / square_size) - 1] == 0:
                    quadrato_x -= square_size
            elif event.key == pygame.K_RIGHT:
                if labirinto[int(quadrato_y / square_size)][int(quadrato_x / square_size) + 1] == 0:
                    quadrato_x += square_size
    
    lab()
   
    pygame.display.flip()