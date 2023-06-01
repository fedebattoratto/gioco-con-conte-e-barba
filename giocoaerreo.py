
import pygame
import random

# Inizializzazione
pygame.init()
pygame.font.init()

# Dimensioni finestra di gioco
width = 800
height = 600



# Colori
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
font2 = pygame.font.SysFont("", 30)
# Creazione finestra di gioco
window = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("gioco mega incredibile")

class Button():
    def _init_(self,x,y,image,scale):
        larghezza = image.get_width()
        altezza = image.get_height()
        self.image = pygame.transform.scale(image,(int(larghezza * scale)),int(altezza * scale))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.cliccato = False
    def draw(self,screen):
        azione = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.cliccato == False:
                self.cliccato = True
                azione = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.cliccato = False



# Caricamento immagini
sfondo=pygame.image.load("sfondo.png")
sfondo=pygame.transform.scale(sfondo, (1000, 800))
airplane_img = pygame.image.load("biplano.png")
airplane_img=pygame.transform.scale(airplane_img, (90, 52))
airplane_img=pygame.transform.flip(airplane_img, True, False)
missile_img = pygame.image.load("missile.png")
missile_img=pygame.transform.scale(missile_img, (40, 40))
missile_img=pygame.transform.flip(missile_img, True, False)
resume_img = pygame.image.load("Resume.png")
options_img = pygame.image.load("option.jpg")
quit_img = pygame.image.load("quit.png")
gameover=pygame.image.load("gameover.png").convert()

#bottoni


# Posizione iniziale dell'aereo
airplane_x = 50
airplane_y = height // 2

# Velocità dell'aereo
airplane_speed = 3

# Lista dei missili
missiles = []
punti=0

def draw_gameover():   
    window.blit(gameover, (300,300))
    pygame.display.flip()

# Funzione per generare nuovi missili
def generate_missile():
    missile_y = random.randint(0, height - missile_img.get_height())
    missile_x = width
    missiles.append([missile_x, missile_y])

# Funzione per disegnare gli oggetti sulla finestra di gioco
def draw_objects():
    window.fill(black)
    window.blit(sfondo, (0,0))
    punti_render=font2.render(str(punti), 1, (0,0,0))

    window.blit(punti_render, (644, 0))
   
    window.blit(airplane_img, (airplane_x, airplane_y))
    for missile in missiles:
        window.blit(missile_img, (missile[0], missile[1]))
    pygame.display.update()

# Ciclo di gioco
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()

    # Movimento dell'aereo
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        airplane_y -= airplane_speed
    if keys[pygame.K_DOWN]:
        airplane_y += airplane_speed
    if keys[pygame.K_LEFT]:
        airplane_x-=airplane_speed


    if keys[pygame.K_RIGHT]:
        airplane_x+=airplane_speed


    # Movimento dei missili
    for missile in missiles:
        missile[0] -= 5

        # Collisione con l'aereo
        if (
            missile[0] < airplane_x + airplane_img.get_width()
            and missile[0] + missile_img.get_width() > airplane_x
            and missile[1] < airplane_y + airplane_img.get_height()
            and missile[1] + missile_img.get_height() > airplane_y
        ):
            game_over = True
        

        # Rimozione dei missili usciti dalla finestra di gioco
        if missile[0] + missile_img.get_width() < 0:
            missiles.remove(missile)

    # Generazione casuale di nuovi missili
    if random.randint(0, 100) < 5:
        generate_missile()

    # Disegno degli oggetti
    draw_objects()
    punti+=1
    

    # Limitazione del framerate a 60 FPS
    clock.tick(60)

# Terminazione del gioco
draw_gameover()
pygame.time.wait(2000)
pygame.quit()