# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 17:13:56 2022

@author: Riccardo Sala
"""
import sys
import os
import random
import time
import pandas as pd

from player import*
from art import *
from items import *
from functions import *
from world import *


# health, armor, cover, hunger, hydra, heat, sanity, energy
player =Carachter(100,0,0,100,100,100,100,100)
          
def main():
    os.system('cls')
    intro()

if __name__ == '__main__':
    main()
    
    
