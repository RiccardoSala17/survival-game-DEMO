# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 12:22:00 2022

@author: Riccardo Sala

"""


# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:00:46 2022

@author: leonardo
"""



class Items(object):
    def __init__(self, name, weight, tier, free_use, combat_use, consumable, descr):
        self.name = name
        self.weight = weight
        self.tier = tier
        self.free_use = free_use
        self.combat_use = combat_use
        self.consumable = consumable
        self.descr = descr
        
        
      
class Weapons(Items):
    def __init__(self, name, weight, tier, free_use, combat_use, consumable, ammo, ammo_type, damage, w_strenght_bonus, w_r_acc_bonus,
                 w_m_acc_bonus, w_char_bonus, w_int_bonus, descr):
        self.damage = damage
        self.w_strenght_bonus = w_strenght_bonus
        self.w_r_acc_bonus = w_r_acc_bonus
        self.w_m_acc_bonus = w_m_acc_bonus
        self.w_char_bonus = w_char_bonus
        self.ammo = ammo
        self.ammo_type = ammo_type
        self.w_int_bonus = w_int_bonus
        super().__init__(name, weight, tier, free_use, combat_use, consumable, descr)
        
class Consumables(Items):
    def __init__(self, name, weight, tier, free_use, combat_use, consumable, health_heal, hunger_heal, hydra_heal, 
                 sanity_heal, energy_heal, descr):
        self.health_heal = health_heal
        self.hunger_heal = hunger_heal
        self.hydra_heal =  hydra_heal
        self.sanity_heal = sanity_heal
        self.energy_heal = energy_heal
        super().__init__(name, weight, tier, free_use, combat_use, consumable, descr)
        
class Drugs(Consumables):
    def __init__(self, name, weight, tier, free_use, combat_use, consumable, health_heal, hunger_heal, hydra_heal, 
                 sanity_heal, energy_heal, poison_heal, bleed_heal, descr):
        self.poison_heal = poison_heal
        self.bleed_heal = bleed_heal
        super().__init__(name, weight, tier, free_use, combat_use, consumable, health_heal, hunger_heal, 
                     hydra_heal, sanity_heal, energy_heal, descr)
    
        
class Food(Consumables):
    def __init__(self, name, weight, tier, free_use, combat_use, consumable, health_heal, hunger_heal, 
                 hydra_heal, sanity_heal, energy_heal, safe, descr):
        self.safe = safe
        super().__init__( name, weight, tier, free_use, combat_use, consumable, health_heal, hunger_heal, 
                     hydra_heal, sanity_heal, energy_heal, descr)

        
class Armor(Items):
    def __init__(self, name, weight, tier, free_use, combat_use, consumable, a_strenght_bonus, a_r_acc_bonus,
                 a_m_acc_bonus, a_char_bonus, arm_bonus, cloth_bonus, arm_check, descr):
        self.a_strenght_bonus = a_strenght_bonus
        self.a_r_acc_bonus = a_r_acc_bonus
        self.a_m_acc_bonus = a_m_acc_bonus
        self.a_char_bonus = a_char_bonus
        self.arm_bonus = arm_bonus
        self.cloth_bonus = cloth_bonus
        self.arm_check = arm_check
        super().__init__(name, weight, tier, free_use, combat_use, consumable, descr)
        
class Resources(Items):
    def __init__(self, name, weight, tier, free_use, combat_use, consumable, descr):
        super().__init__( name, weight, tier, free_use, combat_use, consumable,descr)
        
class Trinkets(Items): 
    def __init__(self, name, weight, tier, free_use, combat_use, consumable, descr):
        super().__init__(name, weight, tier, free_use, combat_use, consumable,descr)
        

        
        
'''
def showStats():
    # Shows item statistics to the player
    item = input("Lookup item stats for: ").lower()

    if item in item_stats:
        print(f"\n{item_stats[item][0]}: Damage: {item_stats[item][1]} Defence: {item_stats[item][2]} "
              f"Rarity: {item_stats[item][3]}")

    else:
        print("Invalid item.")


def equip():
    # This function allows the user to equip items from inventory to the equipped items dict
    item = input("Which item to equip? ").lower()
    for i in PlayerClass.char.inventory:
        try:
            if item == i.name.lower():
                type_of_item = i.i_type
                # Add item to inventory, before replacing in equipped
                if PlayerClass.char.equipped_items[type_of_item] is not None:
                    PlayerClass.char.inventory.append(PlayerClass.char.equipped_items[type_of_item])
                PlayerClass.char.equipped_items[type_of_item] = i

                # Adjust player statistics
                PlayerClass.char.hp += i.health
                PlayerClass.char.defence += i.defence

                print(f"\n{i.name} is now equipped")
                PlayerClass.char.inventory.remove(i)
        except AttributeError:
            pass


def unequip():
    # This function acts as the opposite to the equip function.
    item = input("Which item to unequip? Helmet/Chest/Weapon/Shield ").lower().capitalize()
    if item in ['Helmet', 'Chest', 'Weapon', 'Shield']:
        i = PlayerClass.char.equipped_items[item]

        # Adjust stats for character without item
        PlayerClass.char.hp -= i.health
        PlayerClass.char.defence -= i.defence

        PlayerClass.char.equipped_items[item] = None
        print(f"\n{i.name} is now unequipped")
        PlayerClass.char.inventory.append(i)
    else:
        print("Please select one of the available options.")                
'''        
        

#Weapons list:             name, weight, tier, freeuse, combatuse, consumable, ammo, ammotype, damage, strbonus,raccbonus, maccbonus, charbonus, intimidation, descr,

beretta_9mm = Weapons('beretta 9mm', 1.2, 2, False, True, False, True, 'proiettile 9mm', 10,0,0,0,0,0, "Pistola italiana prediletta da poliziotti e militari. Letale ed efficace.")
vecchio_revolver = Weapons('vecchio revolver .38',1.5, 1, False, True, False, True, 'proiettile .38',8,0,0,0,0,0, "Vecchio revolver di contrabbando, Meglio di niente.")
coltello_cucina = Weapons('coltello da cucina', 0.1, 1, False, True, False, False, None, 2,0,0,0,0,0, "Banale coltello da cucina. Meglio usarlo contro del buon cibo.")
coltello_caccia = Weapons('coltello da caccia', 0.3, 1, False, True, False, False, None, 4,0,0,0,0,0, "Coltello per ogni uso. Difesa personale compresa.")
machete = Weapons('machete', 0.5, 2, False, True, False, False, None, 5,0,0,0,0,0, "Ideale per tagliare gli arbusti. O le persone.")
tubo_piombo = Weapons('tubo di piombo', 3, 2, False, True, False, False, None, 7,0,0,0,0,0, "Pesante tubo di piombo. Sfonda crani e scatole chiuse.")
fucile_m4 = Weapons('fucile automatico M4', 5, 3, False, True, False, True, 'proiettile 5,45mm', 15,0,0,0,0,0, "Fucile automatico militare. Il meglio del meglio.")
katana = Weapons('katana', 2, 3, False, True, False, False, None, 15,0,0,0,0,0, "Spada da guerra affilata come un rasoio. Taglia qualunque cosa.")

#Drugs list:name,weight, tier, freeuse, combatuse, consumable, health,hunger,hydra,sanity,energy,poison,bleed, descr,

benda_leggera = Drugs('benda leggera', 0.1, 1, True, False, True, 10,0,0,0,0,False,True, "Piccola benda, ferma il sanguinamento")
cocaina = Drugs("cocaina",0.1,2,True,False,True,-10,-10,-10,-10,60,False,False, "Cocaina di buona qualità. Ti terrà sveglio per giorni!")
marijuana = Drugs("marijuana",0.1,2,True,False,True,0,-20,0,50,-20,False,False, "Un gustoso spinello mantiene sereni in un mondo senza speranza.")
antidolorifico =Drugs('antidolorifico',0.1,1,True,False,True,30,-10,-10,20,-10,False,False, "Pastiglie di un farmaco oppiaceo. Non abusarne.")
kit_medico_deluxe =Drugs('kit medico deluxe',1.5,3,True,False,True,90,0,0,0,0,True,True, "Il non-plus-ultra della medicina d'emergenza. Cura di tutto.")
bottiglia_grappa =Drugs('bottiglia di grappa',1.5,3,True,False,True,0,-10,-20,80,-10,False,False, "Una bella sbronza cura ogni cattivo pensiero.")
#Food list: name,weight,tier,free_use,combat_use,cons, health, hunger, hyd, sanity, energy, safe, descr

bottiglia_acqua_piccola = Food("bottiglia d'acqua piccola",0.5,1,True,False,True,0,0,15,0,0, True, "Piccola bottiglia d'acqua. Può fare la differenza.")
bottiglia_acqua_media = Food("bottiglia d'acqua media",1,2,True,False,True,0,0,30,0,0,True, "Bottiglia d'acqua. Niente di più.")
bottiglia_acqua_grande= Food("bottiglia d'acqua grande",2,3,True,False,True,0,0,70,0,0,True, "Bottiglia d'acqua grande. Vale tanto oro quanto pesa.")
bottiglia_acqua_piccola_sporca = Food("bottiglia d'acqua piccola sporca",0.5,1,True,False,True,0,0,15,0,0, False, "Meglio purificarla.")
bottiglia_acqua_media_sporca = Food("bottiglia d'acqua media sporca",1,2,True,False,True,0,0,30,0,0,False, "Meglio purificarla.")
bottiglia_acqua_grande_sporca = Food("bottiglia d'acqua grande sporca",2,3,True,False,True,0,0,70,0,0,False, "Meglio purificarla.")
razione_piccola =Food("razione piccola",0.5,1,True,False,True,0,15,0,0,0,True, "Un piccolo spuntino in più può fare la differenza.")
razione_media =Food("razione media",1,2,True,False,True,0,30,0,0,0,True, "L'equivalente di un pasto completo.")
razione_grande =Food("razione grande",2,3,True,False,True,0,70,0,20,0,True, "Pietanza da grande occasione. Rinfranca lo spirito.")
carne_coniglio=Food("coniglio crudo",3,1,True,False,True,0,0,20,0,0,False, "Carne cruda di coniglio. Meglio cuocerla.")
carne_fagiano=Food("fagiano crudo",2,1,True,False,True,0,0,20,0,0,False, "Carne cruda di fagiano. Meglio cuocerla.")
carne_cinghiale=Food("cinghiale crudo",6,2,True,False,True,0,40,0,0,0,False, "Carne cruda di cinghiale. Meglio cuocerla.")
carne_carnivoro = Food("carne di carnivoro",3,2,True,False,True,0,30,0,0,0,False, "Carne cruda di animale carnivoro. Meglio cuocerla.")

#Armor list: name, weight, tier, free_use, combat_use, consumable, strbonus,raccbonus m_acc_bonus, charbonus, armbonus, clothbonus, armcheck, descr
    
giubbotto_antiproiettile_civile = Armor('giubbotto antiproiettile da civile', 5, 2, False, False, False, 0,0,0,0,2,2, True, "Giubbotto antiproiettile scadente. Si trova anche al supermercato.")
giubbino_leggero = Armor("giubbino leggero",0.5,1, False, False, False,0,0,0,0,0,1, False, "Giubbino primaverile in poliestere. Più bello che utile.")

#Resources list: name, weight, tier, free_use, combat_use, consumable, descr
proiettile_9mm = Resources('proiettile 9mm',0.0,1,False,False,True, "Proiettile per pistole e mitra 9mm.")
proiettile_38 = Resources('proiettile .38',0.0,1,False,False,True, "Proiettile per revolver .38.")
proiettile_545 = Resources('proiettile 5,45mm',0.0,1,False,False,True, "Proiettile per fucile automatico 5,45mm")
fiammifero =Resources('fiammifero',0.0,1,False,False,True, "Indispensabile per accendere un fuoco.")
chiodi = Resources('chiodi',0.5,1,False,False,True, "Chiodi di ferro. Utili per costruire oggetti.")
nastro_isolante = Resources('nastro isolante',0.0,1,False,False,True, "Nastro adesivo resistente. Utile per costruire oggetti.")
benzina = Resources('benzina',0.5,1,False,False,True,"Difficile trovare un'auto funzionante, meglio usarla in altri modi.")
rottami_ferro = Resources('rottami di ferro',1,1,False,False,True, "Pezzi di ferro misti. Utili per construire oggetti.")
pezzo_legno = Resources('pezzo di legno',1,1,False,False,True, "Brucialo per scaldarti o usalo per costruire oggetti.")
pelle = Resources('pelle di animale',1,1,False,False,True, "Pelle di animale selvatico. Utile per costruire oggetti.")

straccio = Resources('straccio',0.1,1,False,False,True, "Scampolo di tessuto. Utile per costruire oggetti.")
pastiglia_purif =Resources('pastiglia depurazione acqua',0.1,1,False,False,True, "Purifica fino a 2 litri d'acqua. Una manna dal cielo.") 

#Trinkets list: name, weight, tier, free_use, combat_use, consumable, descr

distintivo = Trinkets('distintivo',0.1,1,False,False,False, "Non esiste più alcuna legge. Ma qualcuno potrebbe non ricordarselo.")
binocolo = Trinkets('binocolo',1.5,1,False,False,False, "Permette di orientarsi senza perdite di tempo.")
sacco_pelo_vecchio = Trinkets('sacco a pelo vecchio',3,1,False,False,False, "Brutto e rovinato, ma protegge ancora i tuoi sonni.")
sacco_pelo_termico = Trinkets('sacco a pelo termico',2,2,False,False,False, "Comprato e mai utilizzato. Ti scalda, ma non è molto comodo.")
sacco_pelo_imbottito = Trinkets('sacco a pelo imbottino',3,3,False,False,False, "Caldo e morbido. Come un abbraccio.")
trappola_piccola = Trinkets('trappola piccola',2,1,False,False,False, "Permette di catturare selvaggina di piccola taglia.")
bastone_viaggio = Trinkets('bastone da viaggio',2,1,False,False,False, "Fai meno fatica quando viaggi. Ed è anche di pregevole fattura.")

#liste di oggetti
weaponT1_list = [coltello_caccia, coltello_cucina, coltello_cucina, coltello_cucina, vecchio_revolver, proiettile_38, proiettile_38, proiettile_38]
weaponT2_list = [machete,machete,tubo_piombo, tubo_piombo, beretta_9mm, proiettile_9mm,proiettile_9mm,proiettile_9mm,proiettile_9mm]
weaponT3_list = [fucile_m4,katana, proiettile_545,proiettile_545,proiettile_545,proiettile_545]

drugsT1_list = []
drugsT2_list = []
drugsT3_list = []

foodT1_list = []
foodT2_list =[]
water_list =[bottiglia_acqua_grande_sporca,bottiglia_acqua_grande, bottiglia_acqua_media_sporca, bottiglia_acqua_media_sporca, bottiglia_acqua_media,
             bottiglia_acqua_piccola, bottiglia_acqua_piccola_sporca, bottiglia_acqua_piccola_sporca, bottiglia_acqua_piccola,bottiglia_acqua_piccola,
             bottiglia_acqua_piccola, bottiglia_acqua_piccola ]

wild_foodT1_list = [carne_coniglio, carne_fagiano]
wild_foodT2_list =[carne_cinghiale, carne_carnivoro, carne_coniglio, carne_fagiano, carne_coniglio, carne_fagiano]
wild_food_list =[carne_cinghiale, carne_carnivoro, carne_coniglio, carne_fagiano, carne_coniglio, carne_fagiano]

resources_list =[]

trinkets_list =[]



full_loot_list =[machete,machete,tubo_piombo, bastone_viaggio]

half_loot_list = [fiammifero, pezzo_legno]



