
import pygame
from pygame.locals import *


class Handler:
    def render(self,fenetre,niveau,fond,cb):
        fenetre.blit(fond, (0, 0))
        niveau.afficher(fenetre)
        fenetre.blit(cb.direction, (cb.x, cb.y))  # dk.direction = l'image dans la bonne direction
        pygame.display.flip()
