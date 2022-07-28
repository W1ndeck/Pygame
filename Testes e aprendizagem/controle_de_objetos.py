import pygame
from pygame.locals import *
from sys import exit

pygame.init()

larg = 640
alt = 480
x = larg/2
y = alt/2

tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption("Joguinho Python")
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

            # esse caso é so quando vc quer clicar e andar apenas uma vez, 
            # independente se continuar pressionado

        """ if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_s:
                y = y + 20
            if event.key == K_w:
                y = y - 20 """
    if pygame.key.get_pressed()[K_a]:
        x = x - 20

    if pygame.key.get_pressed()[K_d]:
        x = x + 20

    if pygame.key.get_pressed()[K_w]:
        y = y - 20

    if pygame.key.get_pressed()[K_s]:
        y = y + 20

    pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))

    pygame.display.update()
