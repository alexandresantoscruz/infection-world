import random
import sys

import pygame
import os
from pygame.locals import *
from sys import exit
from random import randint

class Character(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.idle = self.spriteIdle()
        #walking = self.spriteWalking()

        self.position = 0
        self.eixoX_character = 15
        self.eixoY_character = 500
        self.image = self.idle[self.position]
        self.image = pygame.transform.scale(self.image, (150, 90))

        self.rect = self.image.get_rect()

        self.rect.topleft = [self.eixoX_character, self.eixoY_character]


    def spriteIdle(self):
        self.spriteIdle = []
        self.spriteIdle.append(pygame.image.load("./sprite/character/idle/img1.png"))
        self.spriteIdle.append(pygame.image.load("./sprite/character/idle/img2.png"))
        self.spriteIdle.append(pygame.image.load("./sprite/character/idle/img3.png"))
        self.spriteIdle.append(pygame.image.load("./sprite/character/idle/img4.png"))
        self.spriteIdle.append(pygame.image.load("./sprite/character/idle/img5.png"))
        self.spriteIdle.append(pygame.image.load("./sprite/character/idle/img6.png"))
        self.spriteIdle.append(pygame.image.load("./sprite/character/idle/img7.png"))
        self.spriteIdle.append(pygame.image.load("./sprite/character/idle/img8.png"))
        self.spriteIdle.append(pygame.image.load("./sprite/character/idle/img9.png"))
        self.spriteIdle.append(pygame.image.load("./sprite/character/idle/img10.png"))
        self.spriteIdle.append(pygame.image.load("./sprite/character/idle/img11.png"))
        self.spriteIdle.append(pygame.image.load("./sprite/character/idle/img12.png"))
        self.spriteIdle.append(pygame.image.load("./sprite/character/idle/img13.png"))
        self.spriteIdle.append(pygame.image.load("./sprite/character/idle/img14.png"))
        self.spriteIdle.append(pygame.image.load("./sprite/character/idle/img15.png"))

        return self.spriteIdle

    def spriteWalking(self):
        self.spriteWalking = []
        self.spriteWalking.append(pygame.image.load("./sprite/character/walking/img1.png"));
        self.spriteWalking.append(pygame.image.load("./sprite/character/walking/img2.png"))
        self.spriteWalking.append(pygame.image.load("./sprite/character/walking/img3.png"))
        self.spriteWalking.append(pygame.image.load("./sprite/character/walking/img4.png"))
        self.spriteWalking.append(pygame.image.load("./sprite/character/walking/img5.png"))
        self.spriteWalking.append(pygame.image.load("./sprite/character/walking/img6.png"))
        self.spriteWalking.append(pygame.image.load("./sprite/character/walking/img7.png"))
        self.spriteWalking.append(pygame.image.load("./sprite/character/walking/img8.png"))
        self.spriteWalking.append(pygame.image.load("./sprite/character/walking/img9.png"))
        self.spriteWalking.append(pygame.image.load("./sprite/character/walking/img10.png"))
        self.spriteWalking.append(pygame.image.load("./sprite/character/walking/img11.png"))
        self.spriteWalking.append(pygame.image.load("./sprite/character/walking/img12.png"))
        self.spriteWalking.append(pygame.image.load("./sprite/character/walking/img13.png"))
        self.spriteWalking.append(pygame.image.load("./sprite/character/walking/img14.png"))
        self.spriteWalking.append(pygame.image.load("./sprite/character/walking/img15.png"))

        return self.spriteWalking

    def update(self, x, y):
        self.position += 1

        if self.position >= len(self.spriteIdle):
            self.position = 0
        else:
            self.image = self.spriteIdle[self.position]
            self.image = pygame.transform.scale(self.image, (150, 90))

            self.rect.topleft = [x, 500]

class Inimigo:
    def __init__(self):
        pass

    def spriteVirus(self):
        self.spriteVirus = []
        self.spriteVirus.append(pygame.image.load("./menu/virus.png"))

        return self.spriteVirus

class Vida:
    def spriteVacina(self):
        self.spriteVacina = []
        self.spriteVacina.append(pygame.image.load("./cenario/vacina.png"))

        return self.spriteVacina

class Game:
    inimigo = Inimigo()
    vida = Vida()
    val = 0
    widthBarLife, heightBarLife = 350, 30

    def __init__(self):
        self.virus = pygame.transform.scale(self.inimigo.spriteVirus()[0], (150, 90))
        self.vida = pygame.transform.scale(self.vida.spriteVacina()[0], (150, 90))

    def sceneMenu(self):
        #Exibição do layout
        logo = pygame.image.load("./menu/logo.png")
        background = pygame.image.load('./sprite/background/street.png')
        sceneMenu = pygame.display.set_mode((1080, 600))
        sceneMenu.blit(background, (1080, 0))
        sceneMenu.blit(logo, (300,0))
        sceneMenu.blit(pygame.font.SysFont("helvetica", 20, True, True).render("- Pressione ENTER para iniciar", True, (255, 255, 255)), (400, 500))

        return sceneMenu

    def soundSceneGame(self):
        # Configuração da música
        pygame.mixer.music.load("./sound/cyber.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

    def sceneGame(self):

        #Exibição do layout
        background = pygame.image.load('./sprite/background/street.png')
        background = pygame.transform.scale(background, (1080, 600))

        sceneGame = pygame.display.set_mode((1080, 600))
        sceneGame.blit(background, (0, 0))

        #pontos = 0
        #sceneGame.blit(pygame.font.SysFont("helvetica", 20, True, True).render(f"Pontos: {pontos}", True, (255, 255, 255)), (900, 50))

        #O vírus circula no mundo do jogo
        eixoY_virus = random.randint(0, 600)
        eixoX_virus = random.randint(0, 900)

        imageVirus = sceneGame.blit(self.virus, (eixoX_virus, eixoY_virus))
        self.character = Character()

        #A vida/vacina está no mundo
        eixoY_vida = random.randint(200, 600)
        eixoX_vida = random.randint(400, 900)

        #Carrega vida na cena
        imagemVida = sceneGame.blit(self.vida, (eixoX_vida, eixoY_vida))
        self.character = Character()

        # Barra progresso da vida
        r, g, b = 57, 255, 20

        if self.widthBarLife <= 100:
            r, g, b = 139, 0, 0


        if imageVirus.colliderect(self.character.image.get_rect()):
            self.widthBarLife -= 20

        if imagemVida.colliderect(self.character.image.get_rect()):
            self.widthBarLife += 20

            if self.widthBarLife > 100:
                self.widthBarLife -20



        pygame.draw.rect(sceneGame, (r, g, b), (100, 30, self.widthBarLife, self.heightBarLife))

        return sceneGame

    def sceneGameOver(self):
        #Configuração do layout
        sceneGameOver = pygame.display.set_mode((1080, 600))
        gameOver = pygame.image.load("./menu/game-over.png")

        #Exibição do texto
        sceneGameOver.blit(gameOver, (300, 0))
        sceneGameOver.blit(pygame.font.SysFont("helvetica", 20, True, True).render("- Pressione a tecla 'Q' para sair", True, (255, 255, 255)), (350, 400))
        sceneGameOver.blit(pygame.font.SysFont("helvetica", 20, True, True).render("- Pressione a tecla 'R' para reiniciar o jogo", True, (255, 255, 255)), (350, 300))

        return sceneGameOver

if __name__ == '__main__':

    game = Game()
    eixoX_virus = 0
    eixoY_virus = 0
    eixoX_saude = 0
    eixoY_saude = 0
    eixoX_character = 0
    eixoY_character = 0

    #relógio
    clock = pygame.time.Clock()

    #Inicializo o pygame
    pygame.init()

    #Crio o personagem
    frameIdle = pygame.sprite.Group()
    character = Character()
    frameIdle.add(character)

    #Cena escolhida
    opcao = 0

    #Inicio o som da cena
    game.soundSceneGame()


    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    opcao = 1

                if event.key == pygame.K_q:
                    sys.exit()

                if event.key == pygame.K_r:
                    opcao = 0

                if event.key == pygame.K_d:
                    eixoX_character = eixoX_character + 15

                if event.key == pygame.K_a:
                    eixoX_character = eixoX_character - 15

            if opcao == 0:
                game.sceneMenu()

            if opcao == 1:

                game.sceneGame()
                frameIdle.draw(game.sceneGame())
                character.update(eixoX_character, eixoY_character)

            if game.widthBarLife <= 0:
                game.sceneGameOver()


            pygame.display.update()
            pygame.display.flip()





