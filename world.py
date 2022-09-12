# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 11:29:59 2022

@author: Riccardo Sala
"""


#               MAP
#
#    a   b    c    d    e    f    g            
#   ---------------------------------      sb = sea border
# 1 |sb|sb00|sb00|sb00|OBOO|sb00|sb|       bb = land border
#   ---------------------------------      Sp = starting point
# 2 |bb|Bo07|Ww03|Bo08|Cc09|Bo09|bb|       OBOO = Objective point
#   ---------------------------------      cc = country and fields
# 3 |bb|Bo06|Vv06|Kk03|Kk04|Cc08|bb|       Vv = villages ad human structures
#    --------------------------------      Bo = woods
# 4 |bb|Cc06|Cc07|Kk01|Kk02|Ff04|bb|       Ff = river and lakes
#   ---------------------------------      Ww = barriers/walls/hordes
# 5 |bb|Vv04|Bo05|Ff02|Ff03|Vv05|bb|       Kk = cities
#    --------------------------------
# 6 |bb|Ww02|Vv03|Ff01|Cc05|Bo04|bb|
#    --------------------------------
# 7 |bb|Bo03|Cc03|Ww01|Vv02|Cc04|bb|
#    --------------------------------
# 8 |bb|Cc01|Vv01|Cc02|Bo01|Bo02|bb|                      
#    --------------------------------
# 9 |bb|bb00|bb00|Sp00|bb00|bb00|bb|
#
#   
#	        Risorse	Acqua Caccia Pericolo Zombie	Banditi
# barriera	Alto	Basso	Basso	Alto	Alto	Basso
# fiume 	Basso	Alto	Alto	Basso	Basso	Basso
# città	    Alto	Alto	Basso	Alto	Alto	Alto
# campi	    Medio	Medio	Medio	Basso	Basso	Medio
# boschi	Basso	Medio	Alto	Basso	Basso	Medio
# villaggio	Medio	Medio	Basso	Medio	Medio	Medio
#


class Location:
    def __init__(self, name, biome, visited, full_loot, half_loot, no_loot, north,east,west,south, sorround, dock_pos):
        self.name = name
        self.biome= biome
        self.visited = False
        self.full_loot = True
        self.half_loot = True
        self.no_loot = False
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.sorround = sorround
        self.dock_pos = dock_pos
        
class starting(Location):
    def __init__(self, resource_chance, water_chance, hunt_chance, danger_chance):
        self.resource_chance = 25
        self.water_chance = 50
        self.hunt_chance = 75
        self.danger_chance = 25
        
class country(Location):
    def __init__(self, resource_chance, water_chance, hunt_chance, danger_chance):
        self.resource_chance = 50
        self.water_chance = 50
        self.hunt_chance = 50
        self.danger_chance = 25
        
class woods(Location):
    def __init__(self, resource_chance, water_chance, hunt_chance, danger_chance):
        self.resource_chance = 25
        self.water_chance = 50
        self.hunt_chance = 75
        self.danger_chance = 25
        
class village(Location):
    def __init__(self, resource_chance, water_chance, hunt_chance, danger_chance):
        self.resource_chance = 50
        self.water_chance = 50
        self.hunt_chance = 25
        self.danger_chance = 40
        
class city(Location):
    def __init__(self, resource_chance, water_chance, hunt_chance, danger_chance):
        self.resource_chance = 75
        self.water_chance = 75
        self.hunt_chance = 25
        self.danger_chance = 60

class river(Location):
    def __init__(self, resource_chance, water_chance, hunt_chance, danger_chance):
        self.resource_chance = 25
        self.water_chance = 100
        self.hunt_chance = 75
        self.danger_chance = 25
        
class Wall(Location):
    def __init__(self, resource_chance, water_chance, hunt_chance, danger_chance):
        self.resource_chance = 90
        self.water_chance = 25
        self.hunt_chance = 25
        self.danger_chance = 60
        
        
        
# Location list: name,biome,visited,full_loot, half_loot, no_loot, nord,est,ovest, sud sorround, pos

Sp00 = Location('Sp00', 'starting', False, True, True, False,'Cc02',None,None,None, "A Nord vedi la campagna, le altre direzioni sono impraticabili.", "Il porto si trova a Nord-Est da qui.")
Cc01 = Location('Cc01', 'country',False,True,True, False,'Bo03','Vv01',None,None,"A Nord vedi un bosco, a Est vedi delle abitazioni, le altre direzioni sono impraticabili.", "Il porto si trova a Nord-Est da qui.")                                             
Cc02 = Location('Cc02', 'country',False,True,True, False,'Ww01','Bo01','Vv01','Sp00',"A Nord vedi un'orda di zombie, a Est vedi un bosco, a Ovest vedi delle abitazioni, a Sud torni al punto di partenza.", "Il porto si trova a Nord-Est da qui.")
Cc03 = Location('Cc03', 'country',False,True,True, False,'Vv03','Ww01','Bo03','Vv01',"A Nord vedi un villaggio, a Est vedi un'orda di zombie, a Ovest vedi un bosco, a Sud vedi un villaggio.", "Il porto si trova a Nord-Est da qui.")
Cc04 = Location('Cc04', 'country',False,True,True, False,'Bo04',None,'Vv02','Bo02',"A Nord vedi un bosco, a Est è impraticabile, a Ovest vedi un villaggio, a Sud vedi un bosco.", "Il porto si trova a Nord-Ovest da qui.")
Cc05 = Location('Cc05', 'country',False,True,True, False,'Ff03','Bo04','Ff01','Vv02',"A Nord vedi il fiume, a Est vedi un bosco, a Ovest vedi il fiume, a Sud vedi un villaggio.", "Il porto si trova esattamente a Nord da qui.")
Cc06 = Location('Cc06', 'country',False,True,True, False,'Bo06','Cc07',None,'Vv04',"A Nord vedi un bosco, a Est vedi la campagna, a Ovest è impraticabile, a Sud vedi un villaggio.", "Il porto si trova a Nord-Est da qui.")
Cc07 = Location('Cc07', 'country',False,True,True, False,'Vv06','Kk01','Cc06','Bo05',"A Nord vedi un villaggio, a Est vedi la città, a Ovest vedi la country, a Sud vedi un bosco.", "Il porto si trova a Nord-Est da qui.")
Cc08 = Location('Cc08', 'country',False,True,True, False,'Bo09',None,'Kk04','Ff04',"A Nord vedi un bosco, a Est è impraticabile, a Ovest vedi la città, a Sud vedi il fiume.", "Il porto si trova a Nord-Ovest da qui.")
Cc09 = Location('Cc09', 'country',False,True,True, False,'OB00','Bo09','Bo08','Kk04',"A Nord vedi il porto, a Est vedi un bosco, a Ovest vedi un bosco, a Sud vedi la città.", "Il porto si trova esattamente a Nord da qui.")
Bo01 = Location('Bo01', 'woods',False,True,True, False,'Vv02','Bo02','Cc02',None,"A Nord vedi un villaggio, a Est vedi un bosco, a Ovest vedi la campagna, a Sud è impraticabile.", "Il porto si trova a esattamente a Nord da qui.")
Bo02 = Location('Bo02', 'woods',False,True,True, False,'Cc04',None,'Bo01',None,"A Nord vedi la campagna, a Ovest vedi un bosco, a Est e Sud è impraticabile", "Il porto si trova a Nord-Ovest da qui.")

'''
Bo03 = Location('Bo01', 'woods',False,True,'Vv02','Bo02','Cc02',None,"A Nord vedi un villaggio, a Est vedi un bosco, a Ovest vedi la campagna, a Sud è impraticabile", "Il porto si trova a esattamente a Nord da qui.")
Bo04 = Location('Bo01', 'woods',False,True,'Vv02','Bo02','Cc02',None,"A Nord vedi un villaggio, a Est vedi un bosco, a Ovest vedi la campagna, a Sud è impraticabile", "Il porto si trova a esattamente a Nord da qui.")
Bo05 = Location('Bo01', 'woods',False,True,'Vv02','Bo02','Cc02',None,"A Nord vedi un villaggio, a Est vedi un bosco, a Ovest vedi la campagna, a Sud è impraticabile", "Il porto si trova a esattamente a Nord da qui.")
Bo06 = Location('Bo01', 'woods',False,True,'Vv02','Bo02','Cc02',None,"A Nord vedi un villaggio, a Est vedi un bosco, a Ovest vedi la campagna, a Sud è impraticabile", "Il porto si trova a esattamente a Nord da qui.")
Bo07 = Location('Bo01', 'woods',False,True,'Vv02','Bo02','Cc02',None,"A Nord vedi un villaggio, a Est vedi un bosco, a Ovest vedi la campagna, a Sud è impraticabile", "Il porto si trova a esattamente a Nord da qui.")
Bo08 = Location('Bo01', 'woods',False,True,'Vv02','Bo02','Cc02',None,"A Nord vedi un villaggio, a Est vedi un bosco, a Ovest vedi la campagna, a Sud è impraticabile", "Il porto si trova a esattamente a Nord da qui.")
Bo09 = Location('Bo01', 'woods',False,True,'Vv02','Bo02','Cc02',None,"A Nord vedi un villaggio, a Est vedi un bosco, a Ovest vedi la campagna, a Sud è impraticabile", "Il porto si trova a esattamente a Nord da qui.")
'''

Vv01= Location('Vv01', 'villaggio',False,True, True, False, 'Cc03','Cc02','Cc01',None,"A Nord, Est e Ovest vedi la campagna, a Sud è impraticabile", "Il porto si trova a Nord-Est da qui.")

'''
Vv02
Vv03
Vv04
Vv05
Vv06        
'''

Ww01 = Location('Ww01', 'barriera',False,True, True, False,'Ff01','Vv02','Cc03','Cc02',"A Nord vedi il fiume, a Est vedi un villaggio, a Ovest e Sud vedi la campagna", "Il porto si trova a Nord-Est da qui.")

'''
Ww02
Ww03
Kk01
Kk02
Kk03
Kk04
Ff01
Ff02
Ff03
Ff04        
'''        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        