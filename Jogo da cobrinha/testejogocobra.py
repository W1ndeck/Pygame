# espero q funcione
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.05)  # volume da musica
musifundo = pygame.mixer.music.load( "BoxCat Games - Battle (Special).mp3")  # define musica
pygame.mixer.music.play(-1)  # o -1 define que é pra repetir a musica
lifesound = pygame.mixer.Sound("smw_1-up.wav")  # barulho pra colisão

larg = 640
alt = 480

xsnake = larg/2
ysnake = alt/2

velocidade = 5
x_controle = velocidade
y_controle = 0

xapple = randint(40, 600)
yapple = randint(50, 430)

pontos = 0

morreu = False

fonte = pygame.font.SysFont("Arial", 40, True, True)

tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption("Joguinho Python")
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5

def reiniciar_jogo():
    global pontos, comprimento_inicial, xsnake, ysnake, xapple, yapple, lista_cobra, lista_cabeca, morreu
    pontos = 0
    comprimento_inicial = 5
    xsnake = larg/2
    ysnake = alt/2
    xapple = randint(40, 600)
    yapple = randint(50, 430)
    lista_cobra = []
    lista_cabeca = []
    morreu = False

def crescer_cobra(lista_cobra):  # leio cada x e Y q a cobra ja teve e desenho na tela
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))


while True:

    relogio.tick(60)
    tela.fill((0, 0, 0))
    mensagem = "Pontos: {}".format(pontos)
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        elif event.type == KEYDOWN:

            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            elif event.key == K_d:
                if x_controle == - velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            elif event.key == K_s:
                if y_controle == - velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
            elif event.key == K_w:
                if y_controle ==  velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0

    # posição atual da cobra mais o ultimo comando, asism ela nunca para
    xsnake += x_controle
    ysnake += y_controle

    snake = pygame.draw.rect(tela, (0, 255, 0), (xsnake, ysnake, 20, 20))
    apple = pygame.draw.rect(tela, (255, 0, 0), (xapple, yapple, 20, 20))

    if snake.colliderect(apple):
        xblue = randint(40, 600)
        yblue = randint(50, 430)
        pontos = pontos + 1
        comprimento_inicial += 1
        xapple = randint(40, 600)
        yapple = randint(50, 430)
        lifesound.play()

    lista_cabeca = []
    # armazeno os valores atuais da cobra numa lista
    lista_cabeca.append(xsnake)
    lista_cabeca.append(ysnake)
    lista_cobra.append(lista_cabeca)  # salvo essa lista numa matriz

    if xsnake > larg:
        xsnake = 0
    if xsnake < 0:
        xsnake = larg
    if ysnake < 0:
        ysnake = alt
    if ysnake > alt:
        ysnake = 0

    if lista_cobra.count(lista_cabeca) > 1:
        mensagem2 = "Game over!! Pressione R para jogar novamente"
        fonte2 = pygame.font.SysFont("Arial", 20, True, True)
        texto_formatado2 = fonte2.render(mensagem2, True, (255, 255, 255))
        ret_text = texto_formatado2.get_rect()
        morreu = True
        
        while morreu:
            tela.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            ret_text.center = (larg//2, alt//2)
            tela.blit(texto_formatado2, ret_text)
            pygame.display.update()



    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    crescer_cobra(lista_cobra)

    tela.blit(texto_formatado, (420, 40))

    pygame.display.update()
