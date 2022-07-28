import pygame
from pygame.locals import *
from sys import exit # importa a função de saida

pygame.init()

larg = 640
alt = 480
x = larg/2
y = 0

tela = pygame.display.set_mode((larg, alt)) # aqui eu crio a variavel janela que pode ser usada em outras coisas
pygame.display.set_caption("Joguinho Python") # nomear a janela
relogio = pygame.time.Clock() # definiar a quantos frames é o jogo

while True: # tudo tem q ser dentro while, define o ciclo do jogo
    relogio.tick(30)
    tela.fill((0, 0, 0)) # cor da tela
    for event in pygame.event.get(): # esse trecho é pra criar nossa janela de saida do jogo
        if event.type == QUIT: 
            pygame.quit()
            exit()
    pygame.draw.circle(tela, (255, 255, 255), (x, y), 40) # objeto criado, no caso um circulo
    if y >= alt:
        y = 0
    y = y + 5


    pygame.display.update() # acho que é isso que da refresh no jogo
