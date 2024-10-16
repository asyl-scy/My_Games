# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 07:27:35 2024

@author: Kara
"""

import jeux_pendu2

logos=print("""Bonjour, 
      C'est le jeu du pendu! Le but est de trouver le bon mot.
      Tu as 10 tentatives!
      """)
score=0
game=True
while game:
    score+=jeux_pendu2.Jeux_pendu()
    choix_conti=input("""\n veux-tu continuer?
                      
                      O=oui \t N=Non
                      
                      ta réponse=""")

    if choix_conti=="O" or choix_conti=="o":
        print("Ok! c'est parti")
        print("score = ",score)
        continue
    elif choix_conti =="N" or  choix_conti =="n":
        print("ça marche. Bonne journée à toi!")
        game=False
    else:
        print("j'imagine que la réponse est non")
        print("score final=",score)
        
        game=False
