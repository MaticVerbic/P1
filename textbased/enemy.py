from random import randint
from random import choice
from textbased.inventory import *
class Enemy:
    def __init__(self, name, level, power, experience, gold, drops):
        self.name = name
        self.level = level
        self.power = power
        self.experience = experience
        self.gold = gold
        self.drops = drops
        self.drop = self.calc_drop()
        self.armor = self.power + (self.level*2)


    def calc_drop(self):
        r = randint(5, 75)
        all_items = [item for item in self.drops if item.droprate >= r]
        return choice(all_items) if all_items else None




hum = [["Barbarian", 25, 40, 50, 50], ["Soldier", 35, 60, 80, 80], ["Thief", 10,  30, 50, 50], ["Wizard", 45, 80, 100, 100],
       ["Dwarf", 35, 60, 120, 120], ["Elves", 45, 80, 100, 100], ["John Cena", 100, 150, 500, 500]]
ani = [["Bear", 5, 20, 10, 10], ["Snake", 1, 10, 5, 5], ["Wolf", 5, 20, 10, 10], ["Boar", 3, 10, 10, 10]]
mag = [["Abomination", 25, 40, 35, 35], ["Banshee", 25, 40, 35, 35], ["Basilisk", 35, 60, 60, 60], ["Centaur", 60, 100, 200, 200],
       ["Cyclops", 45, 80, 200, 200], ["Dragon", 60, 100, 700, 700], ["Drake", 40, 75, 250, 250],
       ["Ettan", 30, 50, 50, 50], ["Faeries", 30, 50, 50, 50], ["Giants", 60, 100, 100, 100],  ["Ghost", 30, 65, 40, 40],
       ["Gnome", 7, 25, 50, 50], ["Goblin", 10, 30, 35, 35], ["Golem", 40, 75, 50, 50], ["Griffin", 45, 80, 95, 95],
       ["Grim Reaper", 60, 100, 250, 250], ["Ghoul", 7, 25, 40, 60, 60], ["Gnolls", 7, 25, 35, 35],
       ["Harpie", 35, 60, 75, 75], ["Cobol", 100, 500, 1000, 1000], ["Leprechaun", 100, 150, 150, 5000]]

d = [weaponsdict, armordict, miscdict, accdict]
drops = [x for i in d for x in i.values()]

humdict = {}
anidict = {}
magdict = {}
for h in hum:
    humdict[h[0]] = Enemy(h[0], h[1], h[2], h[3], h[4], drops)

for a in ani:
    anidict[a[0]] = Enemy(a[0], a[1], a[2], a[3], a[4], drops)

for m in mag:
    magdict[m[0]] = Enemy(m[0], m[1], m[2], m[3], m[4], drops)

'''for h in humdict:
    print(vars(humdict[h]))

for a in anidict:
    print(vars(anidict[a]))

for m in magdict:
    print(vars(magdict[m]))'''