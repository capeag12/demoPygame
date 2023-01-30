import random

import pygame

import Colores


class Juego:
    def __init__(self, width, height):
        self.listaCirculos = []
        self.screenWidth = width
        self.screenHeight = height
        self.bateRect = pygame.Rect(self.screenWidth/2,self.screenHeight-30, 200, 20)
        self.ballRect = pygame.Rect(self.screenWidth/2,self.screenHeight/2, 40,40)


    def guardarCoordenada(self):
        pos = pygame.mouse.get_pos()
        self.listaCirculos.append(pos)

    def iniciarJuego(self):
        pygame.init()
        ventana = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Titulo")
        #ball = pygame.image.load("resources/img/pelota.png")
        #ballrec = ball.get_rect()
        speed = [5,5]
        #ballrec.move_ip(320,450)
        fuente = pygame.font.SysFont("arial",20)
        jugando = True
        while jugando==True:
            self.ballRect = self.ballRect.move(speed)
            #ventana.blit(ball, ballrec)
            pygame.display.flip()
            pygame.time.Clock().tick(60)
            ventana.fill(Colores.BLANCO)
            if self.ballRect.left < 0 or self.ballRect.right > ventana.get_width():
                speed[0] = -speed[0]
            if self.ballRect.top < 0:
                speed[1] = -speed[1]
            if pygame.Rect.colliderect(self.bateRect,self.ballRect)  :
                speed[0] = -random.randint(3,6)
                speed[1] = -random.randint(3,6)
            if self.ballRect.bottom > ventana.get_height():
                texto = fuente.render("Has perdido",True, Colores.Azul)
                ventana.blit(texto, (self.screenWidth/2, self.screenHeight/2))



            pygame.draw.rect(ventana, Colores.ROJO, self.bateRect)
            pygame.draw.circle(ventana, Colores.ROJO, (self.ballRect.left+(self.ballRect.width/2), self.ballRect.top+(self.ballRect.width/2)),self.ballRect.width/2)
            for i in self.listaCirculos:
                pygame.draw.circle(ventana, (255, 6, 67), i, 20)

            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                if self.bateRect.left >= 0:
                    self.bateRect = self.bateRect.move(-2, 0)
            if key[pygame.K_RIGHT]:
                if self.bateRect.right<= ventana.get_width():
                    self.bateRect = self.bateRect.move(2, 0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jugando=False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #self.guardarCoordenada()

                    print(self.ballRect)




juego = Juego(640,480)

juego.iniciarJuego()