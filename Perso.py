#vim:set fileencoding=utf-8
from Constantes import *


import pygame


class Perso:

    velX = 0
    velY = 0

    """Classe permettant de créer un personnage"""

    def __init__(self, droite, gauche, gravite, niveau):

        # Sprites du personnage

        self.droite = pygame.image.load(droite).convert_alpha()
        self.gauche = pygame.image.load(gauche).convert_alpha()

        # Position du personnage en cases et en pixels

        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0

        # Direction par défaut

        self.direction = self.droite

        # Niveau dans lequel le personnage se trouve

        self.niveau = niveau

    def deplacer(self):
        """Methode permettant de déplacer le personnage"""

        if self.case_y < (nombre_sprite_cote - 1):
            if self.niveau.structure[self.case_y + self.velY][self.case_x] != 't':
                self.case_y += self.velY

        if True:
            if self.niveau.structure[self.case_y][self.case_x + self.velX] != 't':
                self.case_x += self.velX

        if self.case_y < 0:
            self.case_y = 0
        if self.case_x < 0:
            self.case_x = 0

        self.x = self.case_x * taille_sprite
        self.y = self.case_y * taille_sprite
        self.direction = self.direction
