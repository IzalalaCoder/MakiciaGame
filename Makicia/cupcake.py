import pygame
import random 

# Une classe qui génère un cupcake
class Cupcake(pygame.sprite.Sprite):
    # Constructeur
    def __init__(self, event, game):
        super().__init__()
        self.velocity = random.randint(1, 3)
        self.image = pygame.image.load('assets/pictures/cupcakekawai.png')
        self.image = pygame.transform.scale(self.image, (110, 70))
        self.rect = self.image.get_rect()
        self.event = event
        self.game = game
        self.rect.x = random.randint(0, self.game.surface.get_width())
        self.rect.y = - random.randint(0, self.game.surface.get_height() + 1000 )
        self.attack = 5
        self.angle = 0
        self.originimag = self.image
    
    
    # Le cupcake tombe du ciel
    def tomber(self):
        self.rect.y += self.velocity 
        self.rouler()
        
        if self.event.game.boom(self, self.event.game.toutMakicia):
            self.event.game.player.dommageMakicia(self.attack)
            self.remove()
        
        if self.rect.y >= self.game.surface.get_height() - 95:
            self.remove()
                
            
    # Supprimer le cupcake
    def remove(self):
        self.event.toutCupcake.remove(self)
         
        if len(self.event.toutCupcake) == 0:
            self.event.razPercent()
            self.event.game.pollueMonstre()
            self.event.game.pollueMonstre()
        
        
    # Le cupcake roule sur lui même lors de la chute
    def rouler(self):
        self.angle += random.randint(1, 5)
        self.image = pygame.transform.rotozoom(self.originimag, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)