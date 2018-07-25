import math
class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience = 1
        self.skill_points = 0
        self.weapons = {}
        self.armor = {}
        self.accessories = []
        self.misc = []
        self.healthitems = []
        self.bonus = []
        self.gold = 100
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
        self.equipped_finger_1 = ""
        self.equipped_finger_2 = ""
        self.equipped_neck = ""
        self.equipped_arm = ""
        self.critrate = 1
        self.killing_blow = 1
        self.power = 1
        self.armor_rate = 1

    def print_stats(self):
        s = ("HP: %s, Max HP: %s, Stamina: %s, Level: %s, Experience: %s, Exp. needed to level: %s, Str: %s, Agi: %s, "
             "Int: %s, Dex: %s, Crit rate: %s%%, Killing blow rate: %s%% "
             % (self.health, self.max_health, self.stamina, self.level, self.experience, self.calc_needed(), self.str,
                self.agi, self.int, self.dex, self.calc_crit(), self.calc_kb()))
        s += ("\nWeapon: %s, Armor: %s, Equipped finger 1: %s, Equipped finger 2: %s, Equipped neck: %s, Equipped arm %s"
              % (self.equipped_weapon or "", self.equipped_armor or "", self.equipped_finger_1  or "",
                 self.equipped_finger_2  or "", self.equipped_neck or "", self.equipped_arm or ""))
        print(s)

    '''
    Experience
    '''
    def calc_needed(self):
        return 990+(self.level * 10)

    def add_xp(self, amount):
        self.experience += amount

    def calc_level(self):
        if self.experience >= self.calc_needed():
            while self.experience >= self.calc_needed():
                self.experience -= self.calc_needed()
                self.level += 1
                if self.level % 5 == 0:
                    self.skill_points += 2
                else :
                    self.skill_points += 1
            return True
        else:
            return False

    def player_choice_stats(self):
        while self.skill_points > 0:
            inp = input("Which stat would you like to increase? [str/dex/agi/int]\n")
            stats = ["str", "dex", "agi", "int"]
            funcs = [self.inc_str, self.inc_dex, self.inc_agi, self.inc_int ]
            ind = stats.index(inp)
            funcs[ind]()
            if inp == "dex":
                self.add_hp()
            self.skill_points -= 1



    '''
    INVENTORY METHODS
    '''

    #Add or remove from inventory
    def app_weapons(self, item):
        self.weapons[item.name] = item
    def app_armor(self, item):
        self.armor[item.name] = item
    def app_health(self, item, amount):
        for i in self.healthitems:
            if i[0] == item:
                i[1] += amount
                return
        else:
            return self.healthitems.append([item, amount])

    def app_misc(self, item, amount):
        for i in self.misc:
            if i[0] == item:
                i[1] += amount
                return
        else:
            self.misc.append([item, amount])

    def app_accessories(self, item, amount):
        for i in self.accessories:
            if i[0] == item:
                i[1] += amount
                return
        else:
            self.accessories.append([item, amount])

    def app_bonus(self, item):
        return self.bonus.append(item)
    def del_weapons(self, item):
        del self.weapons[item.name]
    def del_armor(self, item):
        del self.armor[item.name]
    def del_health(self, item, amount):
        for i in self.healthitems:
            if i[0] == item and i[1] > amount:
                i[1] -= amount
            else:
                self.healthitems.pop(self.healthitems.index(i))
    def del_misc(self, item, amount):
        for i in self.misc:
            if i[0] == item and i[1] > amount:
                i[1] -= amount
            else:
                self.misc.pop(self.misc.index(i))
    def del_accessories(self, item, amount):
        for i in self.accessories:
            if i[0] == item and i[1] > amount:
                i[1] -= amount
            else:
                self.accessories.pop(self.accessories.index(i))
    def del_bonus(self, item):
        del self.bonus[item.name]
    def add_gold(self, amount):
        self.gold += amount
    def del_gold(self, amount):
        self.gold -= amount


    #join inventory for user readability
    def inventory(self):
        inv = []
        s = ""
        if self.weapons:
            inv.append([])
            for item in self.weapons:
                if self.weapons[item].weapon_ability:
                    x = ["{:<5} {}".format(name + ":", self.weapons[item].attributes[name]) for name in self.weapons[item].attributes]
                    inv[len(inv) - 1].append(["Name: " + item.capitalize(), "Attributes: " + ", ".join(x), "Ability: " +
                                              self.weapons[item].weapon_ability["description"]])
                else:
                    x = ["{:<5} {}".format(name + ":", self.weapons[item].attributes[name]) for name in self.weapons[item].attributes]
                    inv[len(inv)-1].append(["Name: " + item.capitalize(), "Attributes: " + ", ".join(x)])
            y = ["{:<5} - {} - {}".format(i[0].title(), i[1].title(), i[2].title()) if len(i) > 2
                else "{:<5} - {}".format(i[0].title(), i[1].title()) for i in inv[len(inv)-1]]

            s += " \nWeapons: \n\t" + " | ".join(y) + " | "
        if self.armor:
            inv.append([])
            for item in self.armor:
                x = ["{:<5} {}".format(name + ":", self.armor[item].attributes[name]) for name in self.armor[item].attributes]
                inv[len(inv)-1].append(["Name: " + item,  "Attributes: " + ", ".join(x)])
                x = ["{:<5} - {}".format(name.title(), att.title()  )for name, att in inv[len(inv)-1]]
            s += " \nArmor: \n\t" + " | ".join(x) + " | "
        if self.healthitems:
            inv.append([])
            for item in self.healthitems:
                inv[len(inv)-1].append(["Name: " +item[0].name, "Health: " + str(item[0].health),  "Amount: " + str(item[1])])

                x = ["{:<5} - {} -  {}".format(name.title(), att.title(), amo  )for name, att, amo in inv[len(inv)-1]]
            s += " \nHealth: \n\t" + " | ".join(x) + " | "
        if self.accessories:
            inv.append([])
            for item in self.accessories:
                x = ["{:<5} {}".format(name + ":", self.accessories[self.accessories.index(item)][0].attributes[name]) for name in self.accessories[self.accessories.index(item)][0].attributes]
                inv[len(inv)-1].append(["Name: " + item[0].name, "Attributes: " + ", ".join(x), "Slot: " + str(item[0].slot).title(),  "Amount: " + str(item[1])])
                x = ["{:<5} - {} - {}  - {}".format(name.title(), att.title(), slot, amount)for name, att, slot, amount in inv[len(inv)-1]]
            s += " \nAccessories: \n\t" + " | ".join(x) + " | "
        if self.misc:
            inv.append([])
            for item in self.misc:
                if item[0].attributes:
                    inv[len(inv)-1].append(["Name: " + item[0].name.title(), "Attributes: " + item[0].attributes,  "Amount: " +str(item[1])])
                else:
                    inv[len(inv)-1].append(["Name: " + item[0].name.title(), "Amount: " + str(item[1])])
                x = ["{:<5} {}".format(name, att  )for name, att in inv[len(inv)-1]]
            s += " \nMisc: \n\t" + " | ".join(x) + " | "
        if s:
            s += (" \nGold: %s" % (self.gold))
        return s

    def print_inv(self):
        print(self.inventory())


    def remove_inv(self, item, amount=0):
        if item.type == "weapon":
            self.del_weapons(item)
        elif item.type == "armor":
            self.del_armor(item)
        elif item.type == "health":
            self.del_health(item, amount)

    def add_inv(self, item, amount=0):
        if item.type == "weapon":
            self.app_weapons(item)
        elif item.type == "armor":
            self.app_armor(item)
        elif item.type == "health":
            self.app_health(item, amount)

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
    def unequip_armor(self):
        self.equipped_armor = ""

    '''
    USE ITEMS
    '''
    def healtitem_get_ammount(self, item):
        for i in self.healthitems:
            if i[0] == item:
                return i
        else:
            return "None"
    def use_health(self, item):
        i = self.healtitem_get_ammount(item)
        if self.health < self.max_health and i != None:
            self.health += i[0].health
            self.del_health(item, 1)
            if self.health > self.max_health:
                self.health = self.max_health

    '''
    STATS
    '''
    def inc_dex(self):
        self.dex += 5
    #adds stam to health
    def add_hp(self):
        self.health = self.health + 5

    def inc_agi(self):
        self.agi += 1

    def inc_str(self):
        self.str += 1

    def inc_int(self):
        self.int += 1


    '''
    CALC CRIT AND KB
    '''
    def calc_crit(self):
        equipped = [[self.equipped_weapon, self.weapons], [self.equipped_armor, self.armor],
                    [self.equipped_arm, self.accessories], [self.equipped_finger_1, self.accessories],
                    [self.equipped_finger_2, self.accessories], [self.equipped_neck, self.accessories]]
        s = 5
        cr = 0
        for item, inv in equipped:
            if item and isinstance(inv, dict):
                item = item.lower()
                if "agi" in inv[item].attributes:
                    s += inv[item].attributes["agi"]
                elif "crit rate" in inv[item].attributes:
                        cr += inv[item].weapon_ability["crit rate"]
                if item in self.weapons:
                    if "agi" in inv[item].weapon_ability:
                        s += inv[item].weapon_ability["agi"]
                    elif "crit rate" in inv[item].weapon_ability:
                        cr += inv[item].weapon_ability["crit rate"]
            elif item and isinstance(inv, list):
                s += sum([x[0].attributes["agi"] for x in inv if "agi" in x[0].attributes and x[0].name == item])
                cr += sum([x[0].attributes["crit rate"] for x in inv if "crit rate" in x[0].attributes and x[0].name == item])


        self.critrate = round(cr + ((s + self.agi)/4), 2) + 1
        return self.critrate

    def calc_kb(self):
        equipped = [[self.equipped_weapon, self.weapons], [self.equipped_armor, self.armor],
                    [self.equipped_arm, self.accessories], [self.equipped_finger_1, self.accessories],
                    [self.equipped_finger_2, self.accessories], [self.equipped_neck, self.accessories]]
        s = 0
        cr = 0
        for item, inv in equipped:
            if item and isinstance(inv, dict):
                item = item.lower()
                if "str" in inv[item].attributes:
                    s += inv[item].attributes["str"]
                if item in self.weapons:
                    if "str" in inv[item].weapon_ability:
                        s += inv[item].weapon_ability["str"]
                    elif "killing blow" in inv[item].weapon_ability:
                        cr += inv[item].weapon_ability["killing blow"]
            elif item and isinstance(inv, list):
                s += sum([x[0].attributes["str"] for x in inv if "str" in x[0].attributes and x[0].name == item])
                cr += sum(
                    [x[0].attributes["killing blow"] for x in inv if "killing blow" in x[0].attributes and x[0].name == item])

        self.killing_blow = round((cr + ((s+self.str)/1.5)), 2)
        return self.killing_blow

    def calc_power(self):
        s = (self.str + self.agi)
        multi = (self.level)/100
        w = self.equipped_weapon.lower()
        if w:
            if "str" in self.weapons[w].attributes:
                s += self.weapons[w].attributes["str"] * 1.75
            elif "agi" in self.weapons[w].attributes:
                s += self.weapons[w].attributes["agi"] * 1.5
            if "str" in self.weapons[w].weapon_ability:
                s += self.weapons[w].weapon_ability["str"] * 1.7
            if "agi" in self.weapons[w].weapon_ability:
                s += self.weapons[w].weapon_ability["agi"] * 1.5
            return int(s + (self.weapons[w].power*multi) ) + 1 if self.level < 50 \
                else int(s + (self.weapons[w].power*multi/1.5) ) + 1
        else:
            return int(s) + 1

    def calc_armor(self):
        equipped = [[self.equipped_weapon, self.weapons], [self.equipped_armor, self.armor],
                    [self.equipped_arm, self.accessories], [self.equipped_finger_1, self.accessories],
                    [self.equipped_finger_2, self.accessories], [self.equipped_neck, self.accessories]]
        ar = 0
        dex = 1 or int(self.dex/2)+1
        if self.equipped_armor:
            ar += self.armor[self.equipped_armor.lower()].attributes["armor"]
        s = self.str
        for item, inv in equipped:
            if item and isinstance(inv, dict):
                item = item.lower()
                if "str" in inv[item].attributes:
                    s += inv[item].attributes["str"]
                if item in self.weapons:
                    if "str" in inv[item].weapon_ability:
                        s += inv[item].weapon_ability["str"]
            elif item and isinstance(inv, list):
                s += sum([x[0].attributes["str"] for x in inv if "str" in x[0].attributes and x[0].name == item])
        return int(((ar + s) /dex))+1

    def set_crit(self):
        self.critrate = self.calc_crit()
    def set_kb(self):
        self.killing_blow = self.calc_kb()
    def set_power(self):
        self.power = self.calc_power()
    def set_armor(self):
        self.armor_rate = self.calc_armor()

    def set_fight(self):
        self.set_crit()
        self.set_kb()
        self.set_armor()
        self.set_power()
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