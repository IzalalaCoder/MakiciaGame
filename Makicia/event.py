import pygame
import time
import random
from cupcake import Cupcake
from yellow import Yellow

# Une classe qui génère la notion d'évènement
class Event():
    # Constructeur de la classe Event
    def __init__(self, game):
        self.percent = 0
        self.speed = 10
        self.level = 0
        self.size = game.surface.get_width() - 50
        self.game = game
        self.toutCupcake = pygame.sprite.Group()
        
        
    # Imprémente la barre d'attente d'evenement
    def impremente(self):
        self.percent += 1 / self.speed
        
    
    # Affiche la barre d'évènement
    def attenteBar(self, surface):
        pygame.draw.rect(surface, (41, 39, 40), [30 , surface.get_height() - 30, surface.get_width() - 50, 10])
        if self.percent <= surface.get_width() - 50:
            pygame.draw.rect(surface, (0, 255, 251), [30, surface.get_height() - 30, self.percent, 10])
        # self.attente_avalanche()
        self.impremente()
          
        
    # Remettre a zero
    def razPercent(self):
        self.percent = 0
        self.level += 1
        
        
    # Retourne si la barre est remplie
    def is_full(self):
        return self.percent > self.size
    
    
    # Verification de la possibilité de déclencher l'avalanche de cupcake
    def attente_avalanche(self):
        if self.is_full() and len(self.game.toutMonstre) < 2 :
            self.avalanche()
            self.razPercent()
            self.game.toutMonstre = pygame.sprite.Group()
            
    
    # Démarre l'avalanche
    def avalanche(self):
        # Apparition du cupcake
        num = random.randint(1, 15)
        for i in range(num):
            self.toutCupcake.add(Cupcake(self, self.game))    