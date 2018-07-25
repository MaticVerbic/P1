from random import randint
import random
from inventory import *

class Vendor:
    def __init__(self, inventory):
        self.inventory = inventory
        self.gold = randint(100, 1500)
        
    def add_inventory(self, price, item):
        self.inventory.append([price, item])
        self.gold -= price

    def remove_inventory(self, price, item):
        self.inventory.remove([price,item])
        self.gold += price


names = ["Osvaldo", "Eusebio", "Robin", "Jarod", "Cary"]
vendorsdict = {}



for name in names:
    inv = []
    r = randint(1, 10)
    for i in range(r):
        rw = random.choice(list(weaponsdict.values()))
        rwl = [rw.price, rw.name]
        ra = random.choice(list(armordict.values()))
        ral = [ra.price, ra.name]
        rnd = randint(1, 3)
        if rnd == 2:
            inv.append(ral)
        else:
            inv.append(rwl)
        #inv.append(random.choice(list(weaponsdict.values())) or random.choice(list(armordict.values())))
    vendorsdict[name] = Vendor(inv)

#or random.choice(armordict.keys())

"""for name in vendorsdict:
    print(name, vendorsdict[name].inventory)"""
