from panier import panier # on importe le composant panier

import  pygame #utilisation du module pygame pour faire les jeux avec python
pygame.init()# pour charger les composants necessaire a utilisation de pygame

#2definir les dimentions
largeur = 800
hauteur = 480

#etape 1 creer la fenetre avec pygame
#permet de choisie les dimensions de la fenetre
ma_fenetre=pygame.display.set_mode((largeur,hauteur))#definit la taille
pygame.display.set_caption("attraper les oeufs")#donner un titre a notre jeu

# maintenir la fenetre du jeu en eveil pour pas qu'elle se ferme
#utiliser une boucle qui se fait tant que la fenetre est ouvers
running = True


#charger l'image de l'arriere plan
fond=pygame.image.load("images/fond.jpg")
# charger l'image du sol
sol=pygame.image.load("images/sol.png")

#3 pour ne pas appuyer a chaque fois sur la touche gauche droite
#3 creer un dictionnaire qui va contenir en temps reel les touches enclenchées par le joueur
touche_active={

}

#2creer le panier du joueur
panier=panier(largeur, hauteur) # nouvelle instance de la classe panier

#tant que la boucle est active, on boucle des instruction a chaque fois
while running:#on pouvais egalement mettre while running==True

    #actualiser toutes les images qui sont sur le jeu
    ma_fenetre.blit(fond,(0,0))#blit permet injecter une image
    ma_fenetre.blit(panier.image,panier.rect)
    ma_fenetre.blit(sol,(0,0))

    #3 detecter quelle est la touche active par le joueur
    if touche_active.get(pygame.K_RIGHT):#si la touche droite est activer
        panier.deplacemrnt_droite()
    elif touche_active.get(pygame.K_LEFT):
        panier.deplacement_gauche()


    #mettre a jour l'ecran
    pygame.display.flip()

    #boucler sur les evenement actif du joueur pour savoir si il va fermer la fenetre ou non
    for evenement in pygame.event.get():#il parcour tout les evenement actif du joueur
        #si l'evenement c'est la fermeture de la fenetre
        if evenement.type == pygame.QUIT:#pygame.Quit c'7 pour la fermeture de la fenetre
            running=False# on arrete la boucle pour que
            quit()#on quitte le jeu

        #si l'evenement est un interaction au clavier
        elif evenement.type==pygame.KEYDOWN:
            #quelle touche est enclenchée
            #if evenement.key ==pygame.K_LEFT:#si touche gauche
               # print("gauche !")
               # panier.deplacement_gauche()
           # elif evenement.key == pygame.K_RIGHT:
               # print("Droite !")
               # panier.deplacemrnt_droite()
                touche_active[evenement.key]=True#la touche est activer
        elif evenement.type==pygame.KEYUP:
            touche_active[evenement.key]=False#la touche est desactivé