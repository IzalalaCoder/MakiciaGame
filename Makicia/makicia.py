import pygame
# import animate
from donut import Donut

# Générer une classe qui gère la notion de joueur
class Makicia(pygame.sprite.Sprite):
    # Constructeur
    def __init__(self, game):
        super().__init__()
        self.life = 100
        self.lifemax = 100
        self.attack =  50
        self.velocity = 1
        self.image = pygame.image.load('assets/pictures/character.png')
        self.image = pygame.transform.scale(self.image, (115, 180))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 195
        self.toutDonut = pygame.sprite.Group()
        self.game = game
        
        
    # Déplacement vers la droite 
    def vaDroite(self):
        if not self.game.boom(self, self.game.toutMonstre):
            self.rect.x += self.velocity
    
    
    # Déplacement vers la gauche
    def vaGauche(self):
        self.rect.x -= self.velocity
        
        
    # Lance un donut
    def lancerDonut(self):
        self.toutDonut.add(Donut(self))
        
        
    # Perte de la vie du joueur
    def dommageMakicia(self, montant):
        if self.life - montant > 0:
            self.life -= montant
        else:
            self.game.gameover()
    
    
    # Santé courante de makicia
    def barreSante(self, surface):
        # La couleur pour la jauge de vie (rouge pour le monstre)
        color = (228,188,124)
        # La couleur de l'arrière plan
        colorback = (128, 128, 128)
        
        # La position de la jauge de vie
        # La largeur de la jauge de vie
        # L'épaisseur de la jauge de vie
        position = [self.rect.x, self.rect.y, self.life, 5]
        positionback = [self.rect.x, self.rect.y, self.lifemax, 5]
        
        # Dessiner la barre
        pygame.draw.rect(surface, colorback, positionback) 
        pygame.draw.rect(surface, color, position)
       
