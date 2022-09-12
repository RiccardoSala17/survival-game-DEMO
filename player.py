# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:23:57 2022

@author: Riccardo Sala
"""

from art import *
from player import *
from items import *
from world import *

line = "\n==============================================================================\n"

class Carachter(object):
    def __init__(self, health, armor, cover, hunger, hydra, heat, sanity, energy):
        self.name = ''
        self.pos = Sp00
        self.health = 100
        self.armor = 0
        self.cover = 0
        self.hunger = 100
        self.hydra = 100
        self.heat = 100
        self.sanity = 100
        self.energy = 100
        self.encumbrance = 0
        self.crafting_ability = False
        self.drugs_ability= False
        self.naturer_ability = False
        self.mind_strenght = False
        self.wet = False
        self.alive = True
        self.poison = False
        self.bleeding = False
        self.sex = ''
        self.job = ''
        self.strenght = 5
        self.r_accuracy = 50
        self.m_accuracy = 50
        self.charisma = 5
        self.intimidation = 50
        self.trust = 50
        self.bitten = False
        self.crippled = False
        self.inventory = [fiammifero,fiammifero,fiammifero, bottiglia_acqua_media, razione_media, razione_media, benda_leggera,antidolorifico, sacco_pelo_vecchio]     
        self.equipped_items = {"arma corpo a corpo": None,
                               "arma a distanza": None,
                               "armatura": None,
                               "vestiti": None
                               }
    
        
    def health_condition(self):
        if self.health >= 75:
            return("Sto benissimo")
        elif self.health >= 50:
            return("Sono ferito")
        elif self.health > 25:
            return("Sono gravemente ferito")
        elif self.health <= 25:
            return("Sto per morire")

    def armor_condition(self):
        if self.armor >= 8:
            return("Sono molto protetto")
        elif self.armor >= 6:
            return("Sono abbastanza protetto")
        elif self.armor >= 4:
            return("Sono leggermente protetto")
        elif self.armor <= 2:
            return("Sono indifeso")
        
    def cover_condition(self):
        if self.cover >= 8:
            return("Sono perfettamente coperto")
        elif self.cover >= 6:
            return("Sono ben coperto")
        elif self.cover >= 4:
            return("Sono poco coperto")
        elif self.cover <= 2:
            return("Sono alla mercè del clima")
        
    def hunger_condition(self):
        if self.hunger >= 75:
            return("Sono sazio")
        elif self.hunger >= 50:
            return("Ho leggermente fame")
        elif self.hunger > 25:
            return("Ho molta fame")
        elif self.hunger <= 25:
            return("Sto per morire di fame")

    def hydra_condition(self):
        if self.hydra >= 75:
            return("Sono completamente idratato")
        elif self.hydra >= 50:
            return("Ho poca sete")
        elif self.hydra > 25:
            return("Ho molta sere")
        elif self.hydra <= 25:
            return("Sto per morire di sete")
        
    def heat_condition(self):
        if self.heat >= 75:
            return("Sono al caldo")
        elif self.heat >= 50:
            return("Ho leggermente freddo")
        elif self.heat > 25:
            return("Ho molto freddo")
        elif self.heat <= 25:
            return("Quasi morto di freddo")

    def sanity_condition(self):
        if self.sanity > 75:
            return("Sono determinato")
        elif self.sanity > 50:
            return("Sono un po' turbato")
        elif self.sanity > 25:
            return("Sono molto turbato")
        elif self.sanity < 25:
            return("Sto impazzendo")

    def energy_condition(self):
        if self.energy >= 75:
            return("Totalmente riposato")
        elif self.energy >= 50:
            return("Sono abbastanza energico")
        elif self.energy > 25:
            return("Sono molto stanco")
        elif self.energy <= 25:
            return("Sto per morire di stanchezza")
    
    def status(self):
        print(line)
        print(self.name + ', ' + self.sex + ' ' + self.job + '\n')    
        print( "Salute: " + str(self.health_condition()))
        print( "Armatura: " + str(self.armor_condition()))
        print( "Vestiario: " + str(self.cover_condition()))
        print( "Fame: " + str(self.hunger_condition()))
        print( "Sete: " + str(self.hydra_condition()))
        print( "Calore: " + str(self.heat_condition()))
        print( "Sanità mentale: " + str(self.sanity_condition()))
        print( "Energia: " + str(self.energy_condition()))
        print(line)
        
         

# sex legenda:   male         female              non binary
#               +20 int       -20 int           -20 int       
#               -20 trust     +20 trust         -20 trust

#class legenda:        medic            policeman             criminal             mechanic                          farmer
#                    drugs ab            str mind ab          drugs ab              impr crafting ab               naturer ab
#                   +2 char              +10 racc             +10 racc             +2 str                         +2 str
#                   +20 trust            +10 int              +10 macc             +15 macc                       +15 macc                  
#                   +2 dmg vs zmb        +10 trust            -30 trust            -1 char                        -1 char
# bonus equip:      [antidolorifico]     [beretta9mm]         [machete]            [tubo di piombo]               [binocolo]
#                   [kit medico deluxe]  [8xpoiettili9mm]     [cocaina]            [chiodi][nastro adesivo]       [bottiglia di grappa]
#                   [coltellocucina]     [distintivo]         [vecchio revolver]   [benzina][rottame di ferro]    [machete]
#                                                             [5proiettili.38]                 
                      




















