#!/usr/bin/python
#vim:set fileencoding=utf-8

from Perso import *
from Handler import *
from Niveau import *

#chargement du fond et de la fenètre
fenetre = pygame.display.set_mode((1500, 900))
fond = pygame.image.load("image/fond-1.png").convert()
choix = 'n1.txt'  # choix(a remplacer par la suite)
niveau = Niveau(choix)
niveau.generer()
niveau.afficher(fenetre)
cb = Perso(droite, gauche, gravite, niveau)  # chargement du perso


continuer = 1
while continuer:

    for event in pygame.event.get():  # On parcourt la liste de tous les evenements recus
        pygame.time.Clock().tick(30)
        if event.type == KEYDOWN:

            if event.key == K_RIGHT:
                Perso.velX = 1

            elif event.key == K_LEFT:
                Perso.velX = -1

            elif event.key == K_DOWN:
                Perso.velY = 1

            elif event.key == K_UP:
                Perso.velY = -1

        if event.type == KEYUP:

            if event.key == K_RIGHT:
                Perso.velX = 0

            elif event.key == K_LEFT:
                Perso.velX = 0

            elif event.key == K_DOWN:
                Perso.velY = 0

            elif event.key == K_UP:
                Perso.velY = 0

    try:
        cb.deplacer()
    except IndexError:
        print("__________________________________________________________________________\n"
              "_  Erreur durant le deplacement du personnage                            _\n"
              "_    Une erreur du type IndexError a eu lieu!                            _\n"
              "_________Nous ne savons malheureusement pas encore à quoi elle est due!  _\n")

    Handler.render(None, fenetre, niveau, fond, cb)
