import pygame
import os

import Colores

def dibujarCirculo(ventana):
    pos = pygame.mouse.get_pos()
    print(pos)
    pygame.draw.circle(ventana,(255,6,67),pos, 20)
    print("Se ha creado")


pygame.init()
#Creo la ventana y establezco sus dimensiones
ventana = pygame.display.set_mode((640,480 ))

pygame.display.set_caption("Ejemplo")

ball = pygame.image.load("resources/img/pelota.png")

ballrec = ball.get_rect()

speed = [4,4]

ballrec.move_ip(0,0)
jugando = True

while jugando==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando=False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            dibujarCirculo(ventana)
            pygame.display.flip()
    ballrec = ballrec.move(speed)

    if ballrec.left<0 or ballrec.right>ventana.get_width():
        speed[0] = -speed[0]
    if ballrec.top<0 or ballrec.bottom>ventana.get_height():
        speed[1] = -speed[1]
    ventana.blit(ball, ballrec)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    ventana.fill(Colores.BLANCO)

