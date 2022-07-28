# espero q funcione
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.05)  # volume da musica
musifundo = pygame.mixer.music.load(
    "BoxCat Games - Battle (Special).mp3")  # define musica
pygame.mixer.music.play(-1)  # o -1 define que é pra repetir a musica
lifesound = pygame.mixer.Sound("smw_1-up.wav")  # barulho pra colisão

larg = 640
alt = 480
xsnake = larg/2
ysnake = alt/2
xapple = randint(40, 600)
yapple = randint(50, 430)
pontos = 0

fonte = pygame.font.SysFont("Arial", 40, True, True)

tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption("Joguinho Python")
relogio = pygame.time.Clock()
listasnake = []


def plusnake(listasnake):
    for XeY in listasnake:
        pygame.draw.rect(tela, (255, 255, 255), (XeY[0], XeY[1], 20, 20))


while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    mensagem = "Pontos: {}".format(pontos)
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        xsnake = xsnake - 20

    if pygame.key.get_pressed()[K_d]:
        xsnake = xsnake + 20

    if pygame.key.get_pressed()[K_w]:
        ysnake = ysnake - 20

    if pygame.key.get_pressed()[K_s]:
        ysnake = ysnake + 20

    snake = pygame.draw.rect(tela, (255, 255, 255), (xsnake, ysnake, 20, 20))
    apple = pygame.draw.rect(tela, (255, 0, 0), (xapple, yapple, 20, 20))

    if snake.colliderect(apple):
        xblue = randint(40, 600)
        yblue = randint(50, 430)
        pontos = pontos + 1
        lifesound.play()

    listahead = []
    listahead.append(xsnake)
    listahead.append(ysnake)

    listasnake.append(listahead)

    plusnake(listasnake)

    tela.blit(texto_formatado, (420, 40))

    pygame.display.update()
