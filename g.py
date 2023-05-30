import pygame

pygame.init()

screen=pygame.display.set_mode((800, 800))

pygame.display.set_caption('gioco')
black=(0, 0, 0)
colore=(255,0,0)
clock=pygame.time.Clock()
FPS=60

pygame.draw.rect(screen, colore, (10,20,100,200), 1)
while True:

    #screen.fill(black)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    pygame.display.flip()
    clock.tick(60)