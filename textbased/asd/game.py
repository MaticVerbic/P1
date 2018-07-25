from player import Player
from Enemy import *
from inventory import *
from npc import *
from fight import Fight
from Story import Story


p = Player("asd")
s = Story(p)
print(s.greeting())
s.chap1()
"""
f = Fight(p, anidict["Rat"])
p.app_weapons(weaponsdict["copper sword"])
p.equip_weapon(p.weapons["copper sword"])
p.app_armor(armordict["cloth armor"])
p.equip_armor(p.armor["cloth armor"])

print(f.fight_c())
print(p.experience)

for name in vendorsdict:
    print(name, vendorsdict[name].inventory)

for w in weaponsdict:
    print(vars(weaponsdict[w]))

for hi in healthitems: 
    print(vars(healthitems[hi]))

for a in armordict:
    print(vars(armordict[a]))

for h in humdict:
    print(vars(humdict[h]))

for a in anidict:
    print(vars(anidict[a]))

for m in magdict:
    print(vars(magdict[m]))"""

input("...")
