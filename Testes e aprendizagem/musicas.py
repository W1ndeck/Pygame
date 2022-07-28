import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.05) #volume da musica
musifundo = pygame.mixer.music.load("BoxCat Games - Battle (Special).mp3") #define musica
pygame.mixer.music.play(-1) #o -1 define que é pra repetir a musica
lifesound = pygame.mixer.Sound("smw_1-up.wav") #barulho pra colisão

larg = 640
alt = 480
x = larg/2
y = alt/2
xblue = randint(40, 600)  
yblue = randint(50, 430)
pontos = 0

fonte = pygame.font.SysFont("Arial", 40, True, True) 

tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption("Joguinho Python")
relogio = pygame.time.Clock()

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
        x = x - 20

    if pygame.key.get_pressed()[K_d]:
        x = x + 20

    if pygame.key.get_pressed()[K_w]:
        y = y - 20

    if pygame.key.get_pressed()[K_s]:
        y = y + 20

    ret_red = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    ret_blue = pygame.draw.rect(tela, (0, 0, 255), (xblue, yblue, 40, 50))

    if ret_red.colliderect(ret_blue):  
        xblue = randint(40, 600)
        yblue = randint(50, 430)
        pontos = pontos + 1
        lifesound.play()
        
    tela.blit(texto_formatado, (420,40)) 
    pygame.display.update()