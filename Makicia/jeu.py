import pygame
import time
from makicia import Makicia
from monstre import Monstre
from yellow import Yellow
from event import Event

# Génère la notion de jeu
class Jeu:
    # Constructeur
    def __init__(self, surface):
        self.isplay = False
        self.surface = surface
        self.manage = Event(self)
        # Joueur
        self.toutMakicia = pygame.sprite.Group()
        self.player =  Makicia(self)
        self.toutMakicia.add(self.player)
        self.pressed = {}
        self.score = 0 
        # Monstre
        self.toutMonstre = pygame.sprite.Group()

    
    # Mise à jour du jeu 
    def update(self):
        # Application de l'image du joueur
        self.surface.blit(self.player.image, self.player.rect)
        
        # print(self.pressed)
        # print(self.player.rect.x)
        
        # Actualiser la barre du joueur
        self.player.barreSante(self.surface)
        
        # Actualiser la barre d'evenement
        self.manage.attenteBar(self.surface)
        
        # Appliquer l'ensemble des donuts
        self.player.toutDonut.draw(self.surface)
        
        # Appliquer l'ensemble des monstres
        self.toutMonstre.draw(self.surface)
        
        # Appliquer l'ensemble des cupcakes
        self.manage.toutCupcake.draw(self.surface)
        
        # Récupération des donuts du joueurs
        for donut in self.player.toutDonut:
            donut.deplacement()
            
        # Récupérer les monstres du jeu
        for monster in self.toutMonstre:
            monster.avant()
            monster.barSante(self.surface)
        
        # Récupérer les cupcakes du jeu 
        for cup in self.manage.toutCupcake:
            cup.tomber()
        
        # Vérification de la direction souhaitée par Makicia
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < self.surface.get_width() : 
            self.player.vaDroite()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.vaGauche()
        elif self.pressed.get(pygame.K_f):                
            self.player.lancerDonut()
    
    
    # Démarre le jeu
    def starting(self):
        self.isplay = True
        self.pollueMonstre()
        self.pollueMonstre()
    
    
    # Génère des monstre dans notre jeu
    def pollueMonstre(self):
        monster = Monstre(self)
        self.toutMonstre.add(monster)
    
    
    # Test si il y a une colision    
    def boom(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    
    # Génère le gameover du joueur
    def gameover(self):
        self.manage.toutCupcake = pygame.sprite.Group()
        self.toutMonstre = pygame.sprite.Group()
        self.player.life = self.player.lifemax
        self.isplay = False
        self.score = 0
        self.manage.razPercent()
        