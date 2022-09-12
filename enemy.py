# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:04:51 2022

@author: Riccardo Sala
"""
from items import *
import random


class Enemy(object):
    def __init__(self, name, tier, health, damage, acc, human, drop):
        self.name = name
        self.tier = tier
        self.health = health
        self.damage = damage
        self.acc = acc
        self.human = human
        self.drop = drop

        
class Bandit(Enemy):
    def __init__(self, name, tier, health, damage, acc, human, decept, drop):
        self.decept = decept
        super().__init__(name, tier, health, damage, acc, human, drop) 
    
class Zombie(Enemy):  
    def __init__(self, name, tier, health, damage, acc, human, b_chance, drop):
        self.b_chance = b_chance
        super().__init__(name, tier, health, damage, acc, human, drop) 
    
    
class Animal(Enemy):
    def __init__(self, name, tier, health, damage, acc, human, bleed, poison, drop):
        self.bleed = bleed
        self.poison = bleed
        



            

#Bandit list: name, tier, health, damage, acc, human, decept, drop 

sciacallo = Bandit('sciacallo',1,10,5,40,True,20, [straccio, razione_piccola, bottiglia_acqua_piccola, coltello_caccia, 
                                                   benda_leggera, proiettile_38, proiettile_38, proiettile_9mm, proiettile_9mm])


#Zombie list: name, tier, health, damage, acc, human, b_chance, drop  
zombie_marcio = Zombie('zombie marcio', 1, 8, 2, 30, False, 5, [straccio, razione_piccola, bottiglia_acqua_piccola, coltello_caccia, 
                                                   benda_leggera, proiettile_38, proiettile_38, proiettile_9mm, proiettile_9mm])


#Animal list: name, tier, health, damage, acc, human,bleed, poison, drop            
cane_randagio = Animal('cane randagio',1, 8, 3, 40, False, True, False, [pelle,pelle,pelle, carne_carnivoro, carne_carnivoro, carne_carnivoro])






banditT1_list = []
banditT2_list = []
banditT3_list = []

zombieT1_list = []
zombieT1_list = []
zombieT1_list = []

animal_list = []

woods_animal_list = []






















