# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 19:16:56 2024

@author: Kara

C'est le jeu du pendu.

"""

import numpy as np
import random
    
def Jeux_pendu():
    def inilist(lenght):
        liste=[]
        for i in range(length):
            liste.append("_")
        return liste
    
    def verif_input(choix):
        if choix=="STORY":
            print(story)
        if len(choix)>1:
            return False
        try:
            int(choix)+1
        except:
            return True
        
        return False
    
    
    def verif(choix, story):
        
        for i in story:
            if choix==i:
                print("déjà mis")
                return False
            
        return True
            
            
    
    
    #---------importation
    
    f2=open("dico.txt", "r")
    
    
    
    dico=f2.readlines()
    for i in range(len(dico)):
        dico[i]=dico[i][0:-1]
    
        
    f2.close()
    
    
    #-------------------------------------------------------jeux
    
    #initia
    decision=dico[random.randint(0,len(dico))]
    #print("mon mot a "+str(len(decision))+" lettres")
    #print(decision)
    length=len(decision)
    print("le mot a",length,"lettres")
    print("_ "*length)
    #liste=inilist(length)
    liste=["_" for i in range(length)]
    point=0#pour le score de l'autre programme
    
    #---------------------choix et vérif
    
    game=True
    story=[]
    essai=0
    while game:
        
        #------game over
        if essai==10:
            print("game over(la honte un peu, non?)")
            print('le mot était', decision)
            game=False
            continue
        choix=input("choisi une lettre:\t")
        choix=choix.upper()
        
        
        #-------verification par rapport à l'input
        vf=verif_input(choix)
        if vf==False:
            essai+=1
            print("il te reste",10-essai,"tentatives")
            continue
        
        #------verification par rapport à l'historique
        V=verif(choix,story)
        if V==False :
            essai+=1
            print("il te reste",10-essai,"tentatives")
            continue 
        else:
            story.append(choix)
            
        
        #------affichage bon mot
        marq=0
        for i in range(length):       
    
            if choix==decision[i]:
                liste[i]=str(choix)
                marq+=1
                #essai-=1
        
        
        affiche_liste=""
        for i in liste:
            affiche_liste=affiche_liste+i+" "
        print(affiche_liste)
        
        
        if marq>=1:
            print("il te reste",10-essai,"tentatives")
        else:
            essai+=1
            print("il te reste",10-essai,"tentatives")
            
        
        #----congratulation
        check=0
        for i in liste:
            if i!="_":
                check+=1
            if check==length:
                print("Bien joué à toi!")
                print("""\n En mettant le mot 'Story', tu peux consulter ton historique (hors mots interdits)
                      
                      Attention! C'est compté comme une tentative!""")
                point+=1
                game=False
    
    return point 
        

        

    
