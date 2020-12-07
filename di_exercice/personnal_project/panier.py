import  pygame # importer les comporsans

# creer une classe qui va representer le concept de joueur ou du panier sur notre jeu
class panier(pygame.sprite.Sprite):#sprite definit notre classe comme un composant graghique du jeu et de pouvoir associer une img un graphic etc
    # le constructeur (initialisateur)

    def __init__(self,largeur_ecran,hauteur_ecran):#permet de charger les element du panier
        super().__init__()
        self.nbr_points= 0# nombre de point qu'aura le joueur
        self.image=pygame.image.load("images/panier.png")
        self.image=pygame.transform.scale(self.image,(120,120))#redimentionner l'image
        self.rect=self.image.get_rect()# definir le rectangle autour du panier
        self.rect.x=(largeur_ecran/2)-self.image.get_width()/2
        self.rect.y=(hauteur_ecran-180)
        self.vitesse=6 #vitesse de deplacement panier
        self.largeur_ecran=largeur_ecran
    # methode pour les deplacements
    def deplacemrnt_droite(self):
        if self.rect.x+self.image.get_width()< self.largeur_ecran:

        #si je veux aller a droite on recupere les coordonnes et on ajoute la vitesse
            self.rect.x += self.vitesse
    def deplacement_gauche(self):
        if self.rect.x >0:

            self.rect.x -= self.vitesse
