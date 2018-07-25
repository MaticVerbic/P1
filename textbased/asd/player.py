class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience = 1
        self.weapons = {}
        self.armor = {}
        self.healthitems = []
        self.bonus = []
        self.gold = 0
        self.health = 100
        self.max_health = 100
        self.stamina = 100
        self.mana = 100
        self.str = 1
        self.agi = 1
        self.int = 1
        self.dex = 0
        self.equipped_weapon = ""
        self.equipped_armor = ""

    def print_stats(self):
        s = ("HP: %s, Max HP: %s, Stamina: %s, Level: %s, Experience: %s, Str: %s, Agi: %s, Int: %s, Dex: %s, "
             % (self.health, self.max_health, self.stamina, self.level, self.experience, self.str, self.agi, self.int,
                self.dex))
        s += ("Weapon: %s, Armor: %s" % (self.equipped_weapon, self.equipped_armor))
        print(s)

    '''
    Experience
    '''
    def add_xp(self, amount):
        self.experience += amount

    def calc_level(self):
        if self.xp > 1000:
            self.level += 1
            self.xp -= 1000
            return True
        else:
            return False


    '''
    INVENTORY METHODS
    '''

    #Add or remove from inventory
    def app_weapons(self, item):
        self.weapons[item.name] = item
    def app_armor(self, item):
        self.armor[item.name] = item
    def app_health(self, item):
        return self.healthitems.append(item)
    def app_bonus(self, item):
        return self.bonus.append(item)
    def del_weapons(self, item):
        return self.weapons.remove(item)
    def del_armor(self, item):
        return self.armor.remove(item)
    def del_health(self, item):
        return self.healthitems.remove(item)
    def del_bonus(self, item):
        return self.bonus.remove(item)
    def add_gold(self, amount):
        self.gold += amount
    def del_gold(self, amount):
        self.gold -= amount


    #join inventory for user readability
    def inventory(self):
        inv = [[], [], [], [], [("gold: %s" % (self.gold))]]
        for item in self.weapons.values():
            inv[0].append([item.name, item.attributes])
        for item in self.armor.values():
            inv[1].append([item.name, item.attributes])
        for item in self.healthitems:
            inv[2].append([item.name, item.health])
        return inv
    def print_inv(self):
        print(self.inventory())
    '''
    EQUIP ITEMS
    '''
    def equip_weapon(self, item):
        if item.name in self.weapons:
            self.equipped_weapon = item.name.title()
        else:
            print("That weapon is not in your inventory!")
    def unequip_weapon(self):
        self.equipped_weapon = ""

    def equip_armor(self, item):
        if item.name in self.armor:
            self.equipped_armor = item.name.title()
        else:
            print("That armor is not in your inventory!")
    def unequip_weapon(self):
        self.equipped_armor = ""

    '''
    USE ITEMS
    '''
    def use_health(self, item):
        #item = Healthitems
        if self.health < self.max_health:
            self.health += item.health
            if self.health > self.max_health:
                self.health = self.max_health

    '''
    STATS
    '''
    def inc_dex(self):
        self.dex += 5

    #adds stam to health
    def add_hp(self):
        self.health = 100 + self.dex

    def inc_agi(self):
        self.agi += 1

    def inc_str(self):
        self.str += 1

    def inc_int(self):
        self.int += 1


'''
p = Player("asd")
print(vars(p))
p.app_armor("chain")
print(p.inventory())
p.equip_weapon("chain")
print(p.equipped_armor)
#p.unequip_weapon()
#print(p.equipped_weapon)
p.inc_str()
p.inc_dex()
p.inc_agi()
p.inc_int()
p.add_hp()
p.add_gold(500)
p.del_gold(250)
print(vars(p))
'''