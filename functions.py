# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 09:48:58 2022

@author: Riccardo Sala
"""
import os
import sys
import random

from art import *
from player import *
from items import *
from world import *
from Zombie_Survive import *
from enemy import *

line = "\n==============================================================================\n"

def printHelp():
    print(show_help)
    input("Premi qualunque tasto per andare avanti...")
    os.system('cls')
    print(show_commands1)
    input("Premi qualunque tasto per andare avanti...")
    os.system('cls')
    print(show_commands1)
    input("Premi qualunque tasto per andare avanti...")
    os.system('cls')    


def create_carachter1():
    print(line)
    print("Ti alzi, ti vesti e inizi la tua corsa contro il tempo. Ma il brusco risveglio\n\
ti ha fatto dimenticare anche il tuo nome.")
    print(line)
    user_name = input("Come ti chiami?\n\n> ")
    while user_name == '':
        print('\nNon puoi non avere un nome...\n')
        user_name = input("Come ti chiami?\n\n> ")
    player.name = user_name
    print(line)
    print("Questo è già un buon inizio. Passi davanti a uno specchio sporco e rovinato,\n\
ma riesci con chiarezza a vedere il tuo corpo, il tuo viso e i tuoi pensieri.")
    print(line)
    user_sex = input("Di che sesso sei?\n\n--Digita U per uomo, D per donna e N per non-binary--\n\n> ")
    while user_sex not in ['U','D', 'N', 'u','f','n']:
        print("Comando sconosciuto.\n")
        user_sex = input("Di che sesso sei?\n\n--Digita U per uomo, D per donna e N per non-binary--\n\n> ")
    if user_sex == 'U' or user_sex == 'u':
        player.sex = 'uomo'
        player.intimidation += 20
        player.trust -= 20       
    elif user_sex == 'D' or user_sex == 'd':
        player.sex = 'donna'
        player.intimidation -= 20
        player.trust += 20
    elif user_sex == 'N' or user_sex == 'n':
        player.sex = 'non binary'
        player.intimidation -= 20
        player.trust -= 20
    os.system('cls')
    print(line)
    print("Sei quasi del tutto in te. Continui ad osservarti in quella superficie logora.\n\
Hai ancora addosso i vestiti dall'ultima giornata di lavoro. Non c'era tempo.")
    print(line)
    create_carachter2()

def create_carachter2(): 
    user_job = input("Che lavoro facevi prima dell'invasione?\n\n\
(Puoi scegliere (M) Medico, (P) Poliziotto, (C) Criminale, (W) Meccanico o (K) Contadino.\n\
Se vuoi approfondire i vari lavori digita 'D').\n\n>")
    while user_job not in ['M','P','C', 'W', 'K','D', 'm','p','c','w','k', 'd']:
        print("Comando sconosciuto.\n")
        user_job = input("Che lavoro facevi prima dell'invasione?\n\n\
--Puoi scegliere (M) Medico, (P) Poliziotto, (C) Criminale, (W) Meccanico o (K) Contadino.\n\
Se vuoi approfondire i vari lavori digita 'D'--\n\n>")
    if user_job == 'D' or user_job == 'd':
       print(job_des)
       input("Premi qualunque tasto per andare avanti...")
       os.system('cls')
       print(line)
       create_carachter2()
    elif user_job == 'M' or user_job == 'm':
       player.job = 'medico'
       player.strenght = 5
       player.r_accuracy = 50
       player.m_accuracy = 50
       player.charisma = 7
       player.intimidation = player.intimidation
       player.trust += 20
       player.drugs_ability = True
       add_item(player,antidolorifico, kit_medico_deluxe, coltello_cucina)
      
    elif user_job == 'P' or user_job == 'p':
       player.job = 'poliziotto'
       player.strenght = 5
       player.r_accuracy = 60
       player.m_accuracy = 50
       player.charisma = 5
       player.intimidation += 10 
       player.trust += 10
       player.mind_strenght = True
       add_item(player, beretta_9mm, proiettile_9mm, proiettile_9mm, proiettile_9mm, proiettile_9mm, proiettile_9mm, proiettile_9mm,
                         proiettile_9mm, proiettile_9mm, distintivo)
    
    elif user_job == 'C' or user_job == 'c':
       player.job = 'criminale'
       player.strenght = 5
       player.r_accuracy = 60
       player.m_accuracy = 60
       player.charisma = 5
       player.intimidation = player.intimidation
       player.trust -= 30
       player.drugs_ability = True
       add_item(player,machete, vecchio_revolver, proiettile_38,proiettile_38,proiettile_38,proiettile_38,proiettile_38)

    elif user_job == 'W' or user_job == 'w':
       player.job = 'meccanico'
       player.strenght = 7
       player.r_accuracy = 50
       player.m_accuracy = 65
       player.charisma = 4
       player.intimidation = player.intimidation
       player.trust = player.trust
       player.crafting_ability = True
       add_item(player, tubo_piombo, chiodi, nastro_isolante, benzina, rottami_ferro)
       
    elif user_job == 'K' or user_job == 'k':
       player.job = 'contadino'
       player.strenght = 7
       player.r_accuracy = 50
       player.m_accuracy = 65
       player.charisma = 4
       player.intimidation = player.intimidation
       player.trust = player.trust 
       player.naturer_ability = True
       add_item(player, machete, binocolo, bottiglia_grappa, trappola_piccola)
    print(line)
    print('Ora è chiaro... Sei ' + player.name + ', ' + player.job + ' ' + player.sex)
    print(line)
    input("Premi qualunque tasto per andare avanti...")
    arrival_sp()
       

  
def intro():
    print (art_start1)
    input("Premi qualunque tasto per andare avanti...")
    os.system('cls')
    print(art_start2)
    input("Premi qualunque tasto per andare avanti...")
    os.system('cls')
    print(banner1)
    input("Premi qualunque tasto per andare avanti...")
    os.system('cls')
    create_carachter1()
    input("Premi qualunque tasto per andare avanti...")
    os.system('cls')
    print (art_start3)
    input("Premi qualunque tasto per andare avanti...")
    create_carachter1()

def arrival_sp():
    os.system('cls')
    print(line)
    print("La luce fa male agli occhi. Ti guardi intorno. Solo alberi e case in rovina.\n\
La tua auto è ormai senza vita. Puoi andare subito verso Nord, oppure cercare\n\
cibo o oggetti utili in quest posto desolato. Ora è tutto nelle tue mani.")
    print(line)
    input("Premi qualunque tasto per andare avanti...")
    game_loop() 



def encumbrance_calc():
    inv_weights =[]
    for obj in player.inventory:
        inv_weights.append(obj.weight)
    player.encumbrance = sum(inv_weights)
    return(player.encumbrance)

def add_item(player, *item):
    player.inventory.extend(item)
    
def check_death():
    if player.health <= 0 or player.hunger <= 0 or player.hydra <= 0 or player.heat <= 0 or player.sanity <= 0 or player.energy <= 0:
        game_over()       
    else:
       pass

def game_loop():
    while player.alive == True:
        explore()   
    if player.alive == False:
        print(g_over)
        input("Premi qualunque tasto per andare avanti...")
        sys.exit()

def game_over():
    print(g_over)
    input("Premi qualunque tasto per andare avanti...")
    os.sys('cls')
    print(line)
    retry = input('\nVuoi riprovare? --Y/N--\n' + line + '\n\n> ')
    while retry not in ['Y', 'N','y','n']:
        print("Comando sconosciuto.\n")
        retry = input('\nVuoi riprovare? --Y/N--\n' + line + '\n\n> ')
    if retry == 'Y' or retry == 'y':
        print(line)
        print('\nOttimo, non mollare mai!\n')
        print(line)
        create_carachter1()
        
    elif retry == 'N' or retry == 'n':
        print(line)
        print('\nLa tua famiglia non ti vedrà mai più...\n')
        print(line)
        sys.exit()
    
        
def check_valid_stat(stat):
    if  stat > 100:
        stat = 100
        return stat
    else:
        return stat
  

def explore():
    player.health = check_valid_stat(player.health)
    player.hunger = check_valid_stat(player.hunger)
    player.hydra = check_valid_stat(player.hydra)
    player.heat= check_valid_stat(player.heat)
    player.sanity = check_valid_stat(player.sanity)
    player.energy = check_valid_stat(player.energy)
    check_death()
    print(line)
    my_action = input("Cosa vuoi fare?\n\n\
--Le azioni disponibili sono: (O) orientarsi, (C) cercare, (V) viaggiare,\n\
(K) crafting, (I) inventario, (R) riposare, (P) posizione del porto,\n\
(S) status, (help) aiuto, (exit) esci--\n\n> ")
    while my_action not in ['O','C','V','K','I','R','P','S','HELP','EXIT','o','c','v','k','i','r','s','p','help', 'exit']:
        print("Comando sconosciuto.\n")
        print(line)
        my_action = input("Cosa vuoi fare?\n\n\
--Le azioni disponibili sono: (O) orientarsi, (C) cercare, (V) viaggiare,\n\
(K) crafting, (I) inventario, (R) riposare, (P) posizione del porto,\n\
(S) status, (help) aiuto, (exit) esci--\n\n> ")
    if my_action == 'O' or my_action == 'o':
        orienting()
    elif my_action == 'C' or my_action == 'c':
        searching(player.pos.biome)
    elif my_action == 'V' or my_action == 'v':
        travel()
    elif my_action == 'K' or my_action == 'k':
        crafting()
    elif my_action == 'I' or my_action == 'i':
        inventory()
    elif my_action == 'R' or my_action == 'r':
        rest()
    elif my_action == 'P' or my_action == 'p':
        dock_position()    
    elif my_action == 'S' or my_action == 's':
        player.status()
    elif my_action == 'HELP' or  my_action == 'help':
         printHelp()
    elif my_action == 'EXIT' or my_action == 'exit':
         sys.exit()             
        

def orienting():
    print(line)
    print("Cerchi i punti migliori per osservare il paesaggio...\n")
    if binocolo in player.inventory:
        print("Facile come bere un bicchier d'acqua!\n\n" + player.pos.sorround)
    else:
        print("Ti ci è voluto un del tempo e un bel po' di energie...\n\n" + player.pos.sorround)
        player.hunger -= 5
        player.hydra -= 5
        player.sanity -= 5
        player.energy -= 5
        if player.cover >=4:
            pass
        else:
            player.heat -= 5
    print(line)
    input("Premi qualunque tasto per andare avanti...")
    os.system('cls')

        
def dock_position():
    print(line)
    print('Guardi per qualche secondo la tua bussola...\n')
    print(player.pos.dock_pos)
    print(line)
    input("Premi qualunque tasto per andare avanti...")
    os.system('cls')
    

def travel():
    print(line)
    my_move = input('In che direzione vuoi andare?\n\n\
--Scrivi (N) per nord, (E) per est, (O) per ovest, (S) per sud--\n\n> ')
    while my_move not in ['N','E', 'O', 'S', 'M', 'n','e','o','s','m']:
        print("Comando sconosciuto.\n")
        print(line)
        my_move = input("In che direzione vuoi andare?\n\n\
--Scrivi (N) per nord, (E) per est, (O) per ovest, (S) per sud,\n\
    (M) per tornare al menù esplorazione--\n\n> ")
    
    if my_move == 'M' or my_move == 'm':
        explore()
    else:
        if my_move == 'N' or my_move == 'n':
            try: 
                player.pos = eval(player.pos.north)
            except TypeError:
                print('\nNon puoi andare da questa parte')
                travel()
            
        elif my_move == 'E' or my_move == 'e':
            try: 
                player.pos = eval(player.pos.east)
            except TypeError:
                print('\nNon puoi andare da questa parte')
                travel()      
            
        elif my_move == 'O' or my_move == 'o':
            try: 
                player.pos = eval(player.pos.west)
            except TypeError:
                print('\nNon puoi andare da questa parte')
                travel()
            
        elif my_move == 'S' or my_move == 's':
            try: 
                player.pos = eval(player.pos.south)
            except TypeError:
                print('\nNon puoi andare da questa parte')
                travel()
            if player.pos.biome == 'starting':
                print('\nNon conviene tornare indietro...')
                player.pos == Cc02
                explore() 
            else:
                pass
        player.hunger -= 5
        player.sanity -= 5   
        player.hydra -= 5 
        if player.cover >=6:           
            pass
        elif player.cover >=4:
            player.heat -=5
        else:
            player.heat -= 10   
        if bastone_viaggio in player.inventory:
            player.energy -= 5
        else:
            player.energy -= 10
        check_death()
        arrival_disp()
   
def rest():
    print(line)
    print("Ti prepari per la notte...")
    print(line)
    if random.randrange(0,100) < 15:
        print("Qualcuno ti ha trovato! Preparati allo scontro.")
        encounter()
    else:
        pass
    player.hunger -= 10
    player.hydra -= 10
    player.sanity += 10
    if player.cover >=8:           
        pass
    elif player.cover >=6:
        player.heat -= 10
    elif player.cover >=4:
        player.heat -=20
    else:
        player.heat -= 30  
    if sacco_pelo_imbottito in player.inventory:
        player.heat += 60
        player.energy += 90
    elif sacco_pelo_termico in player.inventory:
        player.heat += 40
        player.energy += 60
    elif sacco_pelo_vecchio in player.inventory:
        player.heat += 20
        player.energy += 60
    else:
        player.heat += 0
        player.energy += 40
    
    print(line)
    print("La notte è passata tranquillamente. Puoi riprendere la tua marcia.")
    
        
def searching(biome):
    os.system('cls')
    print(line)
    my_searching = input("Quale risorsa vuoi cercare?\n\n\
--Scrivi (C) per cercare risorse, (K) per cacciare, (A) per cercare acqua,\n\
(M) per tornare al menù esplorazione--\n\n> ")
    while my_searching not in ['C','K','A','M','c','k','a','m']:
        print("Comando sconosciuto.\n")
        print(line)
        _searching = input("Quale risorsa vuoi cercare?\n\n\
--Scrivi (C) per cercare risorse, (K) per cacciare, (A) per cercare acqua,\n\
(M) per tornare al menù esplorazione--\n\n> ")
        if my_searching == 'M' or my_move == 'm':
           explore()
        else:
           
           if my_searching == 'C' or my_move == 'c':
               if random.randrange(0,100) < biome.danger_chance:
                    print('ciao')
                    #encounter()
                    explore()
               else:
                   if player.pos.full_loot == True:
                       if random.randrange(1,100) < 20:
                           loot_event()
                       else:
                           picks = random.randrange(1,5)
                           search_loot = random.choiches(full_loot_list, k = picks)
                           print("Hai trovato: \n")
                           for obj in search_loot:
                               print(obj.name)
                           add_item(player,search_loot)
                           player.pos.full_loot = False
                           player.pos.half_loot = True
                   elif player.pos.half_loot == True:
                       picks = random.randrange(1,3)
                       search_loot = random.choiches(half_loot_list, k = picks)
                       print("Hai trovato: \n")
                       for obj in search_loot:
                           print(obj.name)
                       add_item(player,search_loot)
                       player.pos.half_loot = False
                       player.pos.no_loot = True
                   elif player.pos.no_loot == True:
                       print("Non c'è più nulla da cercare")
               
           elif my_searching == 'K' or my_move == 'k':
              if random.randrange(0,100) < biome.danger_chance:
                   #encounter()
                   explore()
              else:
                  if random.randrange(0,100) < biome.hunt_chance:
                      if trappola_grande in inventory:
                          picks1 = random.randrange(1,3)
                          picks2 = random.randrange(0,2)
                          hunt_loot = random.choices(wild_foodT2_list, k=picks) + random.choices(wild_food_list, k=picks2)
                          print("Hai trovato: \n")
                          for obj in hunt_loot:
                              print(obj.name)
                          add_item(player,hunt_loot)
                          
                      elif trappola_piccola in inventory:
                         picks1 = random.randrange(0,2)
                         picks2 = random.randrange(0,2)
                         hunt_loot = random.choices(wild_foodT1_list, k=picks) + random.choices(wild_food_list, k=picks2)
                         print("Hai trovato: \n")
                         for obj in hunt_loot:
                             print(obj.name)
                         add_item(player,hunt_loot)
                         
                      else:
                         picks1 = random.randrange(1,2)
                         hunt_loot = random.choices(wild_food_list, k=picks1)
                         print("Hai trovato: \n")
                         for obj in hunt_loot:
                             print(obj.name)
                         add_item(player,hunt_loot)
                  else:
                     print("Non hai trovato niente")
                         
               
               
           elif my_searching == 'A' or my_move == 'A':
               if random.randrange(0,100) < biome.danger_chance:
                   #encounter()
                   explore()
               else:
                   if random.randrange(0,100) < biome.water_chance:
                       picks = random.randrange(1,3)
                       water_loot = random.choices(water_list, k=picks)
                       print("Hai trovato: \n")
                       for obj in water_loot:
                           print(obj.name)
                       add_item(player,water_loot)
                   else:
                       print("Non hai trovato niente")
           player.hunger -= 5
           player.hydra -= 5
           player.sanity -= 5
           player.energy -= 5        
               
   
def arrival_disp():
    os.system('cls')  
    print(line)
    if player.pos.biome == 'country':
        print(random.choice(arrival_country_intro))
    elif player.pos.biome == 'woods':
        print(random.choice(arrival_woods_intro))
    elif player.pos.biome == 'village':
        print(random.choice(arrival_village_intro))
    elif player.pos.biome == 'wall':
        print(random.choice(arrival_wall_intro))
    elif player.pos.biome == 'river':
        print(random.choice(arrival_river_intro))
    elif player.pos.biome == 'city':
        print(random.choice(arrival_city_intro))
    elif player.pos.biome == 'destination':
        arrival_dock()
    explore()
            


def enemy_attack(enemy):
    attack_roll = random.randrange(0,100)
    e_accuracy = enemy.acc + (player.encumbrance * 2)
    if attack_roll < e_accuracy:
        print(enemy.name + ' ti ha colpito!')
        player.health = player.health - enemy.damage
        try:            
            bite_roll = random.randrange(1,100)
            if bite_roll < enemy.b_chance:
                print('Sei stato infettato dallo zombie!')
                player.bitten = True
            else:
                pass
        except AttributeError:
            pass
        try:
            if enemy.bleed == True:
               bleed_roll = random.randrange(1,100)
               if bleed_roll < 20:
                   print('Stai sanguinando.')
                   player.bleed = True
               else:
                   pass
        except AttributeError:
            pass
        try:
            if enemy.poison == True:
               poison_roll = random.randrange(1,100)
               if poison_roll < 20:
                   print('Sei stato avvelenato')
                   player.poison = True
               else:
                   pass
        except AttributeError:
            pass            
    else:
        print(enemy.name + ' ti ha mancato!')   
        
'''
def inventory():
    

def player_attack(enemy):
    
    
def arrival_dock():
    
       
    
def crafting():
    
def inventory():
    

                   
'''


    
    
    
    
    
    
    