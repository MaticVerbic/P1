from textbased.asd.towns import Town
from textbased.player import Player
from textbased.enemy import *
from textbased.inventory import *
from textbased.npc import *
from textbased.fight import Fight
from textbased.story import Story
from textbased.save_load import Save_load
from textbased.towns import *

#TODO every 5th level add 2 skill points [X]
#TODO add vendor mechanics [X]
#TODO finish character screen [X]
#TODO add save/load functionality [X]
#TODO fix save/load functionality [X]
#TODO add skills functionality [X] NOTE ADDED TO STORY.CHARACTER USING PLAYER.CALC_LEVEL AND PLAYER.PLAYER_CHOICE_STATS
#TODO dinamically calculate xp needed to level up 1000+(lvl*10) [X]
#TODO fix allowed amount of items in inventory [X]
#TODO fix p.print_inv() [X]
#TODO add weapon abilities [x]
#TODO add drops to enemy, with drop rate [X]
#TODO accessories [x]
#TODO make fights better
#TODO add towns and functionality
#TODO add town quests
#TODO add chapters
#TODO add fixed enemy strength
#TODO add critrate, killing blow rate
#TODO lose xp on death
#TODO crafting -upgrade, material, drops NOTE: added meterial, added weapon slots
#TODO add bonus items
#TODO add exp needed to lvl to char screen


p = Player("asd")
trade = Trade(p, vendorsdict)
t = Town(p, vendorsdict, trade)
s = Story(p, vendorsdict,t)
sl = Save_load(p, vendorsdict)
"""dr = humdict["Thief"].calc_drop()
print("Drop: ", vars(dr) if dr else "No drop")
vr = humdict["Thief"].calc_drop()
print("Drop: ", vars(vr) if dr else "No drop")"""
#print(vars(weaponsdict["master sword of dexterity"]))
"""p.level = 9
t.quest1()
p.app_health(healthitems["major health potion"], 2)
p.print_inv()
p.app_health(healthitems["major health potion"], 2)
p.print_inv()
p.health = 50
p.del_health(healthitems["major health potion"], 4)
p.use_health(healthitems["major health potion"])
p.print_stats()
p.print_inv()
s.chap2()"""

print(p.calc_armor())

p.app_weapons(weaponsdict["copper sword"])
p.app_weapons(weaponsdict["master sword of haste"])
p.app_health(healthitems["major health potion"], 2)
p.app_health(healthitems["major health potion"], 2)
p.app_accessories(accdict["gold necklace"], 2)
p.app_accessories(accdict["small shield"], 2)
p.app_armor(armordict["steel armor"])

p.use_health(healthitems["major health potion"])
p.app_misc(miscdict["weapon upgrade"], 3)
p.app_misc(miscdict["armor upgrade"], 3)
p.app_misc(miscdict["accessory upgrade"], 3)

#p.equip_armor(p.armor["steel armor"])
#p.equip_weapon(p.weapons["master sword of haste"])
p.app_armor(armordict["cloth armor"])
p.equip_armor(p.armor["cloth armor"])

p.app_weapons(weaponsdict["copper sword"])
p.equip_weapon(p.weapons["copper sword"])
p.str = 10
p.agi = 10
p.dex = 10
p.level = 25

f = Fight(p, anidict["Boar"])
f.printall()

"""
print(p.str, p.agi, p.dex,p. level, p.calc_armor())
p.str = 15
p.agi = 15
p.dex = 10
p.level = 35
print(p.str, p.agi, p.dex,p. level, p.calc_armor())
p.str = 20
p.agi = 15
p.dex = 10
p.level = 45
p.calc_armor()
p.calc_crit()
p.calc_kb()
print(p.str, p.agi, p.dex,p. level, p.calc_armor())
p.str = 20
p.agi = 20
p.dex = 10
p.level = 60
p.calc_armor()
p.calc_crit()
p.calc_kb()
print(p.str, p.agi, p.dex, p. level, p.calc_armor())
p.print_stats()
print(p.calc_armor())

p.equip_armor(p.armor["steel armor"])
p.equip_weapon(p.weapons["master sword of haste"])
p.str = 1
p.agi = 1
p.dex = 10
p.level = 1
p.calc_armor()
p.calc_crit()
p.calc_kb()
print(p.str, p.agi, p.dex,p. level, p.calc_armor())

p.str = 10
p.agi = 10
p.dex = 10
p.level = 25
p.calc_armor()
p.calc_crit()
p.calc_kb()
print(p.str, p.agi, p.dex, p. level, p.calc_armor())
p.str = 15
p.agi = 15
p.dex = 10
p.level = 35
p.calc_armor()
p.calc_crit()
p.calc_kb()
print(p.str, p.agi, p.dex, p. level, p.calc_armor())
p.str = 22
p.agi = 23
p.dex = 10
p.level = 45
p.calc_armor()
p.calc_crit()
p.calc_kb()
print(p.str, p.agi,  p.dex,p. level, p.calc_armor())
p.str = 30
p.agi = 30
p.dex = 10
p.level = 60
#p.app_armor()
p.calc_armor()
p.calc_crit()
p.calc_kb()
print(p.str, p.agi, p.dex, p. level, p.calc_armor())
p.print_stats()
print(p.calc_armor())
#p.print_stats()
""""""
p.equipped_neck = "gold necklace"

#p.print_stats()
#p.print_inv()
sl.save()

p.misc = []
p.weapons = []
p.armor = []
p.accessories = []
p.healthitems = []
#print(p.print_inv() or "||")
sl.load()
#p.print_inv()
#p.print_stats()
'''
for x in asd:
    print(x, "{} ".format(x))
    l += "{} ".format(x)
print(l)"""
'''loadchap = sl.current_chapter
chapters = [s.chap0, s.chap1]
for chapter in chapters[loadchap:]:
   chapter()
t.quest1()'''
'''
n = [0, 1]

chaps = [s.chap0, s.chap1]
for i in chaps[loadchap:]:
    try:
        i()
    except:
        print("There was an error, skipped to next chapter. ")
        continue
'''

"""
p.app_weapons(weaponsdict["copper sword"])
p.app_weapons(weaponsdict["master sword"])
p.print_inv()

vendor = vendorsdict["Robin"]
vendor.gold = 1000
v = Trade(vendorsdict["Robin"], p)
v.sell(weaponsdict["copper sword"])
v.sell(weaponsdict["master sword"])
p.print_inv()
vendor = vendorsdict["Robin"]
p.print_inv()

vendor.add_inventory(50, weaponsdict["copper sword"])
print(vendor.inventory)
#v.buy(weaponsdict["copper sword"])
p.print_inv()

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
