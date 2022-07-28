import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

larg = 640
alt = 480
x = larg/2
y = alt/2
xblue = randint(40, 600)  # sortear novos valores pra o retblue mudar de lugar
yblue = randint(50, 430)

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

    if pygame.key.get_pressed()[K_a]:
        x = x - 20

    if pygame.key.get_pressed()[K_d]:
        x = x + 20

    if pygame.key.get_pressed()[K_w]:
        y = y - 20

    if pygame.key.get_pressed()[K_s]:
        y = y + 20

    ret_red = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    ret_blue = pygame.draw.rect(tela, (0, 0, 255), (xblue, yblue, 40, 50))

    if ret_red.colliderect(ret_blue):  # identific ase houve colisão
        xblue = randint(40, 600)
        yblue = randint(50, 430)

    pygame.display.update()
