import pygame
from pygame.locals import*
import sys
import random
import numpy as np

"""
from pygame.locals import*

pygame.init()
fenetre = pygame.display.set_mode((300,300))

pygame.mixer.music.load('son.wav')
pygame.mixer.music.play()

#pour mettre de la musique!
#on va mettre VitMaster de sakuzyo!!!

j'ai enlevé dans tes_jeux_cube_game tout ce qui est inhérent à l'image, pensant à une erreur

modification= faire en sorte que le dash ne face pas perdre (en faisant en sorte par exemple qu'il fait varier la vitesse et nonepa
la position) /fait

Metter une image

faire bouger le gaol /fait

modif 4 changer le rectangle en autre chose (un perso pixelisé par ex)

modif ultime= faire en sorte qu'il y ait pls personnage et/ou plusieurs goals

modif ultime optionnel= obstacles.

edit= faire une fonction pour varier au début la position du goal puis du player .
    =on a réussi à gérer le pas de 0.5, l'erreur venait du game over car les float ne font pas partie du range(nbcol) ou range(nbrow)
    pour gérer ça, on a mit le int, de façon )à ce que la machine fasse l'approximation
"""

#tiempo

#rect(positionx,positiony, taille, taille)

def show_grid():
    """sert à montrer la grille"""
    for i in range(0, NB_COL):
        for j in range(0, NB_ROW):
            rect = pygame.Rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, pygame.Color("black"), rect, width=1)

def score_musique (score):#relancer la musique si on pert
    """sert à remettre la musique en cas de perte """
    if score==0:
        pygame.mixer.music.play(-1, 0.0, 0)

def high_s(score, highscore):
    """sert a configurer le meilleur score"""
    if score> highscore:
        return score
    else:
        return highscore



class Block:
    # sert à dessiner les blocs (utile pour la phase "3")
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos


class player:
    """la classe du joueur"""
    def __init__(self):
        # position en x/y
        x = 3
        y = 3
        self.block = Block(x, y)
        self.direction = "DOWN"
        
    def draw_player(self):
        """fonction qui sert à dessiner le bloc du joueur"""
        rect = pygame.Rect(self.block.x * CELL_SIZE, self.block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (72, 212, 98), rect)  # lieu ou il sera dessiné, colo et ce qu'on dessine

    def mvt_player(self):
        """fonction qui sert à initialiser les mouvements du joueur"""
        posi = self.block
        varia=1        # conséquence de la touche clavier sur le joueur
        # quoi qu'il se passe, on met y+1, le déplacement diagonal est plus fluide que le déplacement horizontal puis vertical (source=moi)
        if self.direction == "DOWN":
            self.block = Block(self.block.x, self.block.y + varia)
        if self.direction == "RIGHT":
            self.block = Block(self.block.x + varia, self.block.y + varia)
        if self.direction == "LEFT":
            self.block = Block(self.block.x - varia, self.block.y + varia)
        if self.direction == "DASH":
            self.block = Block(self.block.x , NB_ROW-varia)

        # quoi qu'il se passe, ça finit par descendre
        self.direction = "DOWN"


    def nextlvl_player(self):
        """position du joueur au niveau suivant"""
        x = random.randint(int(NB_COL*0.33), int(NB_COL*0.66))
        y = 3
        self.block = Block(x, y)


    def reroll_player(self):
        """position du joueur après une défaite"""
        x = 3
        y = 3
        self.block = Block(x, y)



class goal():
    """classe de l'endroit où doit aller le joueur (goal)"""
    def __init__(self):
        # position en x/y
        x = NB_COL/2
        y = NB_ROW-0.2
        self.block = Block(x, y)

    def draw_goal(self):
        """fonction qui sert à dessiner le bloc du goal"""
        rect = pygame.Rect(self.block.x * CELL_SIZE, self.block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (0,0,0), rect)



    def reset_goal(self):
        """fonction qui sert à réinitialiser le goal (après une défaite du joueur)"""
        self.x = 3
        self.y = NB_ROW - 0.2
        self.block = Block(self.x, self.y)

    # on change juste les coordonnées quand on réussi un niveau
    def nextlevel_goal(self):
        """fonction qui sert à positionner le goal après un succès du joueur"""
        self.x = random.randint(int(NB_COL*0.33), int(NB_COL*0.66))
        self.y = NB_ROW - 0.2
        self.block = Block(self.x, self.y)


#    def generate_goal(self):



class obstacle():
    """classe des obstacles (les toucher provoque un game over)"""
    def __init__(self,a ,b ,a1,b1,a2,b2):
        # position en x/y
        self.body=[Block(a,b),Block(a1,b1),Block(a2,b2)]#les positions des trois blocs (peut mieux faire en vrai)
        self.attention=(6,7,8,9,16,17,18)#les moments (scores) où il y aura les pièges

    def draw_obstacle(self):
        """fonction qui sert à dessiner les obstacles"""
        for block in self.body:
            x_coord=block.x*CELL_SIZE #essaye de varier cell_size pour voir
            y_coord = block.y * CELL_SIZE
            block_rect=pygame.Rect(x_coord,y_coord,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(screen,(82,177,253),block_rect)






class game():
    """class qui va géré le jeu"""
    def __init__(self):
        self.player=player()
        self.goal= goal()
        self.obstacle=obstacle(2,6,5,6,8,6)
        self.score=0
        self.highscore=0

    def update(self):
        """fonction qui va considérer les nouvelles informations"""
        self.player.mvt_player()#pour avoir la position du snake
        self.check_player_on_goal()
        self.game_over()

    def draw_game_element(self):
        """fonction qui va dessiner le joueur et goal"""
        self.player.draw_player()
        self.goal.draw_goal()
        for i in self.obstacle.attention:
            if self.score ==i:
                self.obstacle.draw_obstacle()


    def check_player_on_goal(self):
        """fonction qui va gérer les cas où le joueur a réussi à toucher la cible (goal)"""
        player_block = self.player.block
        goal_block= self.goal.block
        if player_block.x == goal_block.x and player_block.y == NB_ROW - 1:
            self.player.nextlvl_player()
            if  self.score>7:
                self.goal.nextlevel_goal()
            self.score+=1
            print(self.score)
        #t'as pas mis le else

    def game_over(self):# correct
        """fonction qui va gérer les cas de game over"""
        player_block = self.player.block
        if player_block.x not in range(0, NB_COL) or player_block.y not in range(0, NB_ROW):
            self.player.reroll_player()
            self.goal.reset_goal()
            self.highscore=high_s(self.score, self.highscore)
            self.score=0
            print("gameover_1")
        for i in self.obstacle.body:
            for k in self.obstacle.attention:
                if self.score==k:
                    if self.player.block.x==i.x and self.player.block.y==i.y:
                        self.player.reroll_player()
                        self.goal.reset_goal()
                        self.highscore = high_s(self.score, self.highscore)
                        self.score = 0
                        print("gameover_2")


def vitesse(score):
    if score>=30:
        return 0.4
    elif score>=20:
        return 0.6
    elif score>=12:
        return 0.8
    else:
        return 1


# -----------------------------------------



pygame.init()  # initialisation des modules

# taille écran
#10/15
NB_COL = 10
NB_ROW = 15
CELL_SIZE = 40

#musique
pygame.mixer.music.load('musique/Cytus R - VitMaster - Sakuzyo_Jc7_74J9nmg.mp3')
#pygame.mixer.music.play(-1,0.0,0)
# initialisation écran
screen = pygame.display.set_mode(size=(NB_COL * CELL_SIZE, NB_ROW * CELL_SIZE))
pygame.display.set_caption("save the cat")#titre fenêtre

timer = pygame.time.Clock()

#chargementimage
image = pygame.image.load("image/cyberconcoursv1.png").convert_alpha()
# initialisation jeux
game=game()


#initialisation texte
police=pygame.font.SysFont("",25)


# prendre en compte les touches du joueur
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)  # utilisé pour créer un timer de 200millisec.

game_on = True
pygame.time.get_ticks()
while game_on:
    # pour quitter
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        score_musique(game.score)
        fluctu=vitesse(game.score)
        fluctu2=100*fluctu
        #fluctu2=75
        pygame.time.set_timer(SCREEN_UPDATE,int(fluctu2))  # j'ai dupliqué ici pour penser à le varier pour complexifier le niveau


        if event.type == SCREEN_UPDATE:
            game.update()



        if event.type == pygame.KEYDOWN:  # si l'utilisateur a appuyé sur le clavier
            if event.type == pygame.KEYDOWN:  # si l'utilisateur a appuyé sur le clavier
                if event.key == pygame.K_LEFT:
                    game.player.direction = "LEFT"
                if event.key == pygame.K_RIGHT:
                    game.player.direction = "RIGHT"
                if event.key == pygame.K_DOWN:
                    game.player.direction = "DASH"

    screen.fill(pygame.Color('white'))  # remplir l'écran principal avec une couleur

    #affichage_score
    image_texte = police.render(str(game.score)+"("+str(game.highscore)+")", 1, (255, 0, 0))

    screen.blit(image_texte, (NB_COL, NB_ROW))

    #screen.blit(image, (0, 0))

    show_grid()  # voir la grille
    game.draw_game_element()
    #print(game.player.block.x)
    #print(pygame.time.get_ticks()/1000)#tiempo

    pygame.display.update()  # permettre la mise à jour des données à chaque pas de temps
    timer.tick(200)  # "fps"
    pygame.display.flip()






