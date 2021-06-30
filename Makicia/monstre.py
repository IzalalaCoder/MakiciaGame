import pygame
import random 

# Générer une classe qui génère la notion de monstre
class Monstre(pygame.sprite.Sprite):
    # Constructeur
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.life = 100
        self.lifemax = 100
        self.attack = 0.1
        self.image = pygame.image.load('assets/pictures/red.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 600 + random.randint(100, 1000)
        self.rect.y = 282
        self.divise = 500000
        self.velocity = random.random() / self.divise
    
    
    # La santé courante du monstre
    def barSante(self, surface):
        # La couleur pour la jauge de vie (rouge pour le monstre)
        color = (237,34,82)
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

    
    # Déplacement du monstre
    def avant(self):
        if not self.game.boom(self, self.game.toutMakicia):
            self.rect.x -= self.velocity / self.divise
        else:
            self.game.player.dommageMakicia(self.attack)
    
    
    # Perte de la vie du monstre
    def dommageMonstre(self, montant):
        self.life -= montant
        
        if self.life <= 0:
            self.rect.x = 600 + random.randint(100, 1000)
            self.life = self.lifemax
            self.velocity = random.random() / self.divise
            
            if self.game.manage.is_full():
                self.game.toutMonstre.remove(self)
                self.game.manage.attente_avalanche()