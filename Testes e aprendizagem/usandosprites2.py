import pygame
from pygame.locals import *
from sys import exit

pygame.init()


largura_janela = 640
altura_janela = 480


tela_jogo = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Sprites")
relogio_jogo = pygame.time.Clock()


class Gato(pygame.sprite.Sprite):
    def __init__(self):
        # padrão pra toda classe q tiver sprites essas 3 linhas
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []  # criando lista com as sprites e adicionando todas elas
        self.sprites.append(pygame.image.load("sprites/sprite_gatinho0.png"))
        self.sprites.append(pygame.image.load("sprites/sprite_gatinho1.png"))
        self.sprites.append(pygame.image.load("sprites/sprite_gatinho2.png"))
        self.sprites.append(pygame.image.load("sprites/sprite_gatinho3.png"))
        self.sprites.append(pygame.image.load("sprites/sprite_gatinho4.png"))
        self.sprites.append(pygame.image.load("sprites/sprite_gatinho5.png"))
        self.atual = 0
        self.image = self.sprites[self.atual]
        # aumentando a escala das sprites
        self.image = pygame.transform.scale(self.image, (72*2, 60*2))

        # transformando num quadrado e dizendo onde quero a imagem
        self.rect = self.image.get_rect()
        self.rect.topleft = 300, 330

    def update(self):

        self.atual += 0.15
        if self.atual >= len(self.sprites):
            self.atual = 0

        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (72*2, 60*2))

    def atacar(self):
        self.animar = True


todas_as_sprites = pygame.sprite.Group()
gato = Gato()
todas_as_sprites.add(gato)

imagem_fundo = pygame.image.load("sprites/cidade_fundo.jpg").convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura_janela, altura_janela)) #convertendo a escala pra se adequar a minha tela


while True:

    relogio_jogo.tick(60)  # 60 fps
    tela_jogo.fill((0, 0, 0))  # cor da tela preta

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit()


    tela_jogo.blit(imagem_fundo, (0,0))
    todas_as_sprites.draw(tela_jogo)
    todas_as_sprites.update()
    pygame.display.flip()
