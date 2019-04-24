
import pygame
from pygame.locals import *


class Handler:

    def tick(self,cb):
        for event in pygame.event.get():  # On parcourt la liste de tous les evenements recus
            pygame.time.Clock().tick(30)
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                try:
                    cb.deplacer('droite')
                except:
                    print("erreur")

            elif event.key == K_LEFT:
                try:
                    cb.deplacer('gauche')
                except:
                    print("erreur")

            elif event.key == K_DOWN:
                try:
                     cb.deplacer('gravite')
                except:
                    print("erreur")

            elif event.key == K_UP:
                try:
                    cb.deplacer('antiGravite')
                except:
                    print("erreur")

    def render(self,fenetre,niveau,fond,cb):
        fenetre.blit(fond, (0, 0))
        niveau.afficher(fenetre)
        fenetre.blit(cb.direction, (cb.x, cb.y))  # dk.direction = l'image dans la bonne direction
        pygame.display.flip()
