import pygame
from jeu import Jeu
pygame.init()

# Generer la fenetre du jeu ---------------------------------------------
pygame.display.set_caption("GameMakicia")
img = pygame.image.load('assets/pictures/makicia.jpg')
pygame.display.set_icon(img)
screen = pygame.display.set_mode((700, 400))
game = Jeu(screen)
run = True
background = pygame.image.load('assets/pictures/background.png')

# Une page d'accueil -----------------------------------------------------
titre = pygame.image.load('assets/pictures/titre.png')
titre_rect = titre.get_rect()
titre_rect.x = screen.get_width() // 8
elements = pygame.image.load('assets/pictures/elements.png')
play = pygame.image.load('assets/pictures/play.png')
play = pygame.transform.scale(play, (240, 90))
play_rect = play.get_rect()
play_rect.x = screen.get_width() // 3
play_rect.y = screen.get_height() // 6
setting = pygame.image.load('assets/pictures/settings.png')
setting = pygame.transform.scale(setting, (270, 90))
setting_rect = setting.get_rect()
setting_rect.x = screen.get_width() // 3 - 15
setting_rect.y = screen.get_height() // 3
quit = pygame.image.load('assets/pictures/quit.png')
quit = pygame.transform.scale(quit, (245, 90))
quit_rect = quit.get_rect()
quit_rect.x = screen.get_width() // 3 
quit_rect.y = screen.get_height() - 200
help = pygame.image.load('assets/pictures/help.png')
help = pygame.transform.scale(help, (500, 500))
help_rect = help.get_rect()

# Boucle du jeu -----------------------------------------------------------
while run:
    # Application de l'arrière plan sur la fenetre
    screen.blit(background, (0, 0))
    
    # verifier si notre jeu est commencé
    if game.isplay:
        game.update()
    else:
        screen.blit(titre, titre_rect)
        screen.blit(elements, (0, 270))
        screen.blit(play, play_rect)
        screen.blit(setting, setting_rect)
        screen.blit(quit, quit_rect)
        
    # Mise a jour de l'écran
    pygame.display.flip()
    
    #  si le joueur ferme cette fenêtre
    for e in pygame.event.get() :
        if e.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif e.type == pygame.KEYDOWN:
            # if e.key == pygame.K_RIGHT:
            #     print('Déplacement vers la droite')
            #     game.player.vaDroite()
            # elif e.key == pygame.K_LEFT:
            #     print('Déplacement vers la gauche')
            #     game.player.vaGauche()
            game.pressed[e.key] = True
            # Détection de l'enclenchement de la touche espace
            if e.key == pygame.K_SPACE:
                game.player.lancerDonut()
        elif e.type == pygame.KEYUP:
            game.pressed[e.key] = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            # Vérification des buttons
            if play_rect.collidepoint(e.pos):
                # Lancement du jeu
                game.starting()
            if setting_rect.collidepoint(e.pos):
                print('Option')
                print('BARRE ESPACE - TIRER')
                print('FLECHE DROITE ET GAUCHE - SE DEPLACER')
            if quit_rect.collidepoint(e.pos):
                run = False
                pygame.quit()