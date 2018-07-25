from random import randint
import random
from textbased.inventory import *

class Vendor:
    def __init__(self, inventory, name):
        self.inventory = inventory
        self.gold = randint(100, 1500)
        self.name = name
        
    def add_inventory(self, price, item):
        self.inventory.append([price, item.name])
        self.gold -= price

    def remove_inventory(self, price, item):
        self.inventory.remove([price,item.name])
        self.gold += price


class Trade:
    def __init__(self, v, p):
        self.v = v
        self.p = p

    def item_in_inv(self, item):
        for i in self.p.inventory():
            for n in i:
                if item.name in n:
                    return True
        else:
            return False

    def item_in_inv_v(self, item):
        for i in self.v.inventory:
            if item.name in i:
                return True
        else:
            return False

    def get_price(self, item):
        return item.price

    def calc_money_vendor(self, price):
        if self.v.gold > price:
            return True
        else:
            return False

    def calc_money_player(self, price):
        if self.p.gold > price:
           return True
        else:
            return False

    def sell(self, item):
        if self.item_in_inv(item):
            price = self.get_price(item)
            if self.calc_money_vendor(price):
                self.v.add_inventory(price, item)
                self.p.add_gold(price)
                self.p.remove_inv(item)

            else:
                print("error")
    def buy(self, item):
        if self.item_in_inv_v(item):
            price = self.get_price(item)
            if self.calc_money_vendor(price):
                self.v.remove_inventory(price, item)
                self.p.del_gold(price)
                self.p.add_inv(item)


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
    vendorsdict[name] = Vendor(inv, name)

#or random.choice(armordict.keys())

"""for name in vendorsdict:
    print(name, vendorsdict[name].inventory)"""
