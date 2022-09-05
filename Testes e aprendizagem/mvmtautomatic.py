import pygame
from pygame.locals import *
from sys import exit

pygame.init()


largura_janela = 640
altura_janela = 480


miar = pygame.mixer.Sound("sons/Meow.ogg")
ronronar = pygame.mixer.Sound("sons/cat_mewpurr.wav")

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
        self.sprites.append(pygame.image.load("sprites/gatinho_esquerda0.png"))
        self.sprites.append(pygame.image.load("sprites/gatinho_esquerda1.png"))
        self.sprites.append(pygame.image.load("sprites/gatinho_esquerda2.png"))
        self.sprites.append(pygame.image.load("sprites/gatinho_esquerda3.png"))
        self.sprites.append(pygame.image.load("sprites/gatinho_esquerda4.png"))
        self.sprites.append(pygame.image.load("sprites/gatinho_esquerda5.png"))

        self.atual = 0
        self.image = self.sprites[self.atual]
        # aumentando a escala das sprites
        self.image = pygame.transform.scale(self.image, (72*2, 60*2))

        # transformando num quadrado e dizendo onde quero a imagem
        self.rect = self.image.get_rect()
        self.x = 300
        self.y = 330
        self.rect.topleft = self.x, self.y

        self.andadireita = False
        self.andaesquerda = False

    def update(self):

        if self.andaesquerda == True:
            # self.atual = 0
            self.atual += 0.15
            self.x -= 2
            self.rect.topleft = self.x, self.y

            if self.atual >= (len(self.sprites)/2):
                self.atual = 0
                self.andaesquerda = False

        elif self.andadireita == True:
            if self.atual < 6:  # RECEBAAAAA ESSA GAMBIARRA NO SEU PEITÃO!!!!
                self.atual += 6 - self.atual
            self.atual += 0.15
            self.x += 2
            self.rect.topleft = self.x, self.y
            if self.atual >= len(self.sprites):
                self.atual = 6
                self.andadireita = False

        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (72*2, 60*2))

    def andardireita(self):
        self.andadireita = True
        self.andaesquerda = False

    def andaresquerda(self):
        self.andaesquerda = True
        self.andadireita = False


todas_as_sprites = pygame.sprite.Group()
gato = Gato()
todas_as_sprites.add(gato)

imagem_fundo = pygame.image.load("sprites/cidade_fundo.jpg").convert()
# convertendo a escala pra se adequar a minha tela
imagem_fundo = pygame.transform.scale(
    imagem_fundo, (largura_janela, altura_janela))


while True:

    relogio_jogo.tick(60)  # 60 fps
    tela_jogo.fill((0, 0, 0))  # cor da tela preta

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit()

        if pygame.key.get_pressed()[K_d]:
            gato.andardireita()
        if pygame.key.get_pressed()[K_a]:
            gato.andaresquerda()

        if pygame.key.get_pressed()[K_e]:
            ronronar.play()

        if event.type == KEYDOWN:
            if event.key == K_q:
                miar.play()

    if gato.rect.x > largura_janela - 120:
        gato.rect.x = largura_janela - 120

    if gato.rect.x < 0:
        gato.rect.x = 0

    tela_jogo.blit(imagem_fundo, (0, 0))
    todas_as_sprites.draw(tela_jogo)
    todas_as_sprites.update()
    pygame.display.flip()
