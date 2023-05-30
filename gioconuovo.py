import pygame
import random

sfondo=pygame.image.load('sfondo.png')
biplano=pygame.image.load('biplano.png')
biplano=pygame.transform.scale(biplano, (100, 52))
biplano=pygame.transform.flip(biplano, True, False)

missile=pygame.image.load('missile.png')
missile=pygame.transform.scale(missile, (80, 80))
missile=pygame.transform.flip(missile, True, False)

base=pygame.image.load('base900x100.png')
gameover=pygame.image.load('gameover.png')
loghino=pygame.image.load('loghino.jpg')
loghino=pygame.transform.scale(loghino, (70, 70))


finestra=pygame.display.set_mode((781, 260))

pygame.display.set_caption('er giocone')

FPS=50

avanzamento=3

#FONT = pygame.font.SysFont('comic Sans MS', 50, bold=True)

def inizializza():

    global biplanox, biplanoy

    global basex

    global missili

    global tra_i_missili

    #global punti

    global run
    biplanox, biplanoy= 60, 150

    basex=0
    punti=0
    missili=[]

    missili.append(Missili_classe())

    tra_i_missili=False
    run = True

class Missili_classe:

    def __init__(self):

        self.x=random.randint(800, 950)

        self.y=random.randint(1, 150)

    def scrolling(self):

        self.x=avanzamento

        finestra.blit(missile, (self.x, self.y))

        finestra.blit(missile, (self.x + 150, self.y + 25))

    def collisione(self, biplano, biplanox, biplanoy):
        tolleranza = 5

        biplano_dx=biplanox + biplano.get_width() - tolleranza

        biplano_sx=biplanox + tolleranza

        biplano_giu=biplanoy + biplano.get_height() - tolleranza

        biplano_su=biplanoy + tolleranza

        missili_dx=self.x + missile.get_width() - tolleranza
        missili_sx=self.x
        missili_su=biplanoy + tolleranza
        missili_giu=biplanoy + missile.get_height()

        if biplano_dx > missili_sx and biplano_sx < missili_dx:
            if biplano_su > missili_su and biplano_giu < missili_giu:
                hai_perso()

    def tra_i_missili(self, biplano, biplanoy):

        tolleranza = 5

        biplano_giu =  biplanoy +  biplano.get_width() - tolleranza
        biplano_su=biplanoy + tolleranza

        missili_giu=self.y + missile.get_width()
        missili_su=self.y 

        if biplano_giu > missili_su or biplano_su < missili_giu:
            return True
    
def disegna():
    finestra.blit(sfondo, (0,0))

    for m in missili:
        m.scrolling()

    finestra.blit(biplano, (biplanox, biplanoy))

    finestra.blit(base, (basex, 220))

    #punti_render=FONT.render(str(punti), 1, (255, 0, 0))

    #finestra.blit(punti_render, (644, 0))

    finestra.blit(loghino, (0, 0))

def aggiorna():

    pygame.display.update()

    pygame.time.Clock().tick(FPS)

def hai_perso():
    finestra.blit(gameover, (300, 130))

    aggiorna()

    ricominciamo=False

    while not ricominciamo:
        for event in pygame.event.get():

            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                inizializza()

                ricominciamo=True
            if event.type==pygame.QUIT:
                pygame.quit

inizializza()

while True:
    basex -= avanzamento

    if basex < -120:
        basex=0

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
    
    tasti=pygame.key.get_pressed()

    if tasti[pygame.K_LEFT]:
        biplanox -= 1


    if tasti[pygame.K_RIGHT]:
        biplanox += 1

    if tasti[pygame.K_UP]:
        biplanoy -= 1

    if tasti[pygame.K_DOWN]:
        biplanoy += 1

    if missili[-1].x < 150: 
        missili.append(Missili_classe())

    for m in missili:
        m.collisione(biplano, biplanox, biplanoy)

    if not tra_i_missili:
        for m in missili:
            if m.tra_i_missili(biplano, biplanox):
                tra_i_missili=True
                break
    if biplanoy > 160: 
        hai_perso()

    #punti +=1

    disegna()
    aggiorna()