import pygame

# Générer un donut 
class Donut(pygame.sprite.Sprite):
    # Constructeur
    def __init__(self, makicia):
        super().__init__()
        self.velocity = 1
        self.image = pygame.image.load('assets/pictures/donuts.png')
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.x = makicia.rect.x + 70
        self.rect.y = makicia.rect.y + 120
        self.originimag = self.image
        self.makicia = makicia
        self.angle = 0
        
        
    # Supprime ce donut
    def remove(self):
        self.makicia.toutDonut.remove(self)


    # Le donut se déplace lors du lancer
    def deplacement(self):
        self.rect.x += self.velocity
        self.rouler()
        
        # Verification
        for monster in self.makicia.game.boom(self, self.makicia.game.toutMonstre):
            self.remove() 
            # Dégat 
            monster.dommageMonstre(self.makicia.attack)
        
        if self.rect.x > 700:
            self.makicia.toutDonut.remove(self)
           
           
    # Lors du lancer de donut le donut tourne sur lui même 
    def rouler(self):
        self.angle += 20
        self.image = pygame.transform.rotozoom(self.originimag, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)
        