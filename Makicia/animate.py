import pygame

# Génère les animations (non utilisée dans ce projet)
class Animate(pygame.sprite.Sprite):
    # Constructeur
    def __init__(self, name):
        super().__init__()
        self.image = pygame.image.load('assets/pictures/' + name + '.png')
        self.current = 0    
        self.images = anim.get(name)
        
        
    # Animer le sprite
    def animation(self):
        self.current += 1
        
        if self.current >= len(self.images):
            self.current = 0
        
        self.image = self.images[self.current]


# Fonction de chargement des images
def chargement(dossier ,name):
    img = []
    # Récupération du chemin
    path = "assets/pictures/" + dossier + "/" + name
    extension = ".png"
    for num in range(1, 5):
        pathimg = path + str(num) + extension
        print(pathimg)
        img.append(pygame.image.load(pathimg))
    return img 


# Un banque d'images
# 'character' -> [character1.png, ...]
# 'characterattack' -> [characterattack1.png, ...]
anim = {
    'character' : chargement("character", "character"),
    'characterattack' : chargement("character", "characterattack")
}