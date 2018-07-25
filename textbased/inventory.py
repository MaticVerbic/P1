class Items:
    def __init__(self, name, attributes = "", price=0, health=0, type="", ability="", slot="", droprate=0, power=0, gem_slots=0, weapon_ability={}, crafted_slots={}):
        self.name = name
        self.attributes = attributes
        self.price = price
        self.health = health
        self.type = type
        self.ability = ability
        self.slot = slot
        self.droprate = droprate
        self.power = power
        self.gem_slots = gem_slots
        self.weapon_ability = weapon_ability
        self.crafted_slots = {}

"""{"killing blow": 10, "description": "gives 5% chance for killing blow"}"""

weapons = [["copper sword", {"str": 2, "dex": 1}, 50, 20, 50],
           ["copper sword of strength",   {"str": 2, "dex": 1}, 100, 20,  {"str": 2, "description": "adds 2 strength"}, 40],
           ["copper sword of dexterity",  {"str": 2, "dex": 1}, 100, 20,  {"dex": 2,  "description": "adds 2 dex"}, 40],
           ["copper sword of agility",    {"str": 2, "dex": 1}, 100, 20,  {"agi": 2,  "description": "adds 2 agility"}, 40],
           ["copper sword of intellect",  {"str": 2, "dex": 1}, 100, 20,  {"int": 2,  "description": "adds 2 intellect"}, 40],
           ["copper sword of death",      {"str": 2, "dex": 1}, 100, 20,  {"killing blow": 2, "description": "gives 2% chance for killing blow"}, 40],
           ["copper sword of life",       {"str": 2, "dex": 1}, 100, 20,  {"health": 10, "description": "gives 10 hp"}, 40],
           ["copper sword of haste",      {"str": 2, "dex": 1}, 100, 20,  {"crit rate": 2, "description": "adds 2% to crit rate"}, 40],
           ["iron sword", {"str": 4, "dex": 2}, 100, 40, 40],
           ["iron sword of strength",  {"str": 4, "dex": 2}, 175, 40,  {"str": 5, "description": "adds 5 strength"}, 30],
           ["iron sword of dexterity", {"str": 4, "dex": 2}, 175, 40,  {"dex": 5,  "description": "adds 5 dex"}, 30],
           ["iron sword of agility",   {"str": 4, "dex": 2}, 175, 40,  {"agi": 5,  "description": "adds 5 agility"}, 30],
           ["iron sword of intellect", {"str": 4, "dex": 2}, 175, 40,  {"int": 5,  "description": "adds 5 intellect"}, 30],
           ["iron sword of death",     {"str": 4, "dex": 2}, 175, 40,  {"killing blow": 5, "description": "gives 5% chance for killing blow"}, 30],
           ["iron sword of life",      {"str": 4, "dex": 2}, 175, 40,  {"health": 40, "description": "gives 40 hp"}, 30],
           ["iron sword of haste",     {"str": 4, "dex": 2}, 175, 40,   {"crit rate": 5, "description": "adds 5% to crit rate"}, 30],
           ["steel sword", {"str": 6, "dex": 4}, 200, 80, 30],
           ["steel sword of strength", {"str": 6, "dex": 4}, 200, 80,  {"str": 10, "description": "adds 10 strength"}, 20],
           ["steel sword of dexterity", {"str": 6, "dex": 4}, 200, 80,  {"dex": 10,  "description": "adds 10 dex"}, 20],
           ["steel sword of agility",   {"str": 6, "dex": 4}, 200, 80,  {"agi": 10,  "description": "adds 10 agility"}, 20],
           ["steel sword of intellect", {"str": 6, "dex": 4}, 200, 80,  {"int": 10,  "description": "adds 10 intellect"}, 20],
           ["steel sword of death",     {"str": 6, "dex": 4}, 200, 80,  {"killing blow": 7, "description": "gives 7% chance for killing blow"}, 20],
           ["steel sword of life",      {"str": 6, "dex": 4}, 200, 80,  {"health": 60, "description": "gives 60 hp"}, 20],
           ["steel sword of haste",     {"str": 6, "dex": 4}, 200, 80,   {"crit rate": 7, "description": "adds 7% to crit rate"}, 20],
           ["expert sword", {"str": 15, "dex": 10}, 1000, 200, 10],
           ["expert sword of strength", {"str": 15, "dex": 10}, 1200, 200, {"str": 15, "description": "adds 15 strength"}, 5],
           ["expert sword of dexterity", {"str": 15, "dex": 10}, 1200, 200, {"dex": 15,  "description": "adds 15 dex"}, 5],
           ["expert sword of agility",   {"str": 15, "dex": 10}, 1200, 200, {"agi": 15,  "description": "adds 15 agility"}, 5],
           ["expert sword of intellect", {"str": 15, "dex": 10}, 1200, 200, {"int": 15,  "description": "adds 15 intellect"}, 5],
           ["expert sword of death",     {"str": 15, "dex": 10}, 1200, 200, {"killing blow": 15, "description": "gives 15% chance for killing blow"}, 5],
           ["expert sword of life",      {"str": 15, "dex": 10}, 1200, 200, {"health": 100, "description": "gives 100 hp"}, 5],
           ["expert sword of haste",     {"str": 15, "dex": 10}, 1200, 200,  {"crit rate": 15, "description": "adds 15% to crit rate"}, 5],
           ["master sword", {"str": 10, "dex": 8}, 650, 120, 20],
           ["master sword of strength", {"str": 10, "dex": 8}, 650, 120, {"str": 15, "description": "adds 15 strength"}, 10],
           ["master sword of dexterity", {"str": 10, "dex": 8}, 650, 120, {"dex": 15,  "description": "adds 15 dex"}, 10],
           ["master sword of agility",   {"str": 10, "dex": 8}, 650, 120, {"agi": 15,  "description": "adds 15 agility"}, 10],
           ["master sword of intellect", {"str": 10, "dex": 8}, 650, 120, {"int": 15,  "description": "adds 15 intellect"}, 10],
           ["master sword of death",     {"str": 10, "dex": 8}, 650, 120, {"killing blow": 15, "description": "gives 15% chance for killing blow"}, 10],
           ["master sword of life",      {"str": 10, "dex": 8}, 650, 120, {"health": 100, "description": "gives 100 hp"}, 10],
           ["master sword of haste", {"str": 10, "dex": 8}, 650, 120, {"crit rate": 12, "description": "adds 12% to crit rate"}, 10],
           ["basic bow", {"agi": 2, "dex": 2}, 20, 10, 50],
           ["homemade bow", {"agi": 4, "dex": 2}, 50, 20, 40],
           ["homemade bow of strength", {"agi": 4, "dex": 2}, 100, 20, {"str": 5, "description": "adds 5 strength"}, 30],
           ["homemade bow of dexterity", {"agi": 4, "dex": 2}, 100, 20, {"dex": 5,  "description": "adds 5 dex"}, 30],
           ["homemade bow of agility",   {"agi": 4, "dex": 2}, 100, 20, {"agi": 5,  "description": "adds 5 agility"}, 30],
           ["homemade bow of intellect", {"agi": 4, "dex": 2}, 100, 20, {"int": 5,  "description": "adds 5 intellect"}, 30],
           ["homemade bow of death",     {"agi": 4, "dex": 2}, 100, 20, {"killing blow": 5, "description": "gives 5% chance for killing blow"}, 30],
           ["homemade bow of life",      {"agi": 4, "dex": 2}, 100, 20, {"health": 40, "description": "gives 40 hp"}, 30],
           ["homemade bow of haste",     {"agi": 4, "dex": 2}, 100, 20,  {"crit rate": 5, "description": "adds 5% to crit rate"}, 30],
           ["longbow", {"agi": 8, "dex": 4}, 100, 40, 30],
           ["longbow of strength",  {"agi": 8, "dex": 4}, 175, 40,  {"str": 10, "description": "adds 10 strength"}, 20],
           ["longbow of dexterity", {"agi": 8, "dex": 4}, 175, 40,  {"dex": 10,  "description": "adds 10 dex"}, 20],
           ["longbow of agility",   {"agi": 8, "dex": 4}, 175, 40,  {"agi": 10,  "description": "adds 10 agility"}, 20],
           ["longbow of intellect", {"agi": 8, "dex": 4}, 175, 40,  {"int": 10,  "description": "adds 10 intellect"}, 20],
           ["longbow of death",     {"agi": 8, "dex": 4}, 175, 40,  {"killing blow": 7, "description": "gives 7% chance for killing blow"}, 20],
           ["longbow of life",      {"agi": 8, "dex": 4}, 175, 40,  {"health": 60, "description": "gives 60 hp"}, 20],
           ["longbow of haste",     {"agi": 8, "dex": 4}, 175, 40,   {"crit rate": 7, "description": "adds 7% to crit rate"}, 20],
           ["shortbow", {"agi": 8, "dex": 6}, 200, 80, 20],
           ["shortbow of strength",  {"agi": 8, "dex": 6}, 275, 80,  {"str": 15, "description": "adds 15 strength"}, 10],
           ["shortbow of dexterity", {"agi": 8, "dex": 6}, 275, 80,  {"dex": 15,  "description": "adds 15 dex"}, 10],
           ["shortbow of agility",   {"agi": 8, "dex": 6}, 275, 80,  {"agi": 15,  "description": "adds 15 agility"}, 10],
           ["shortbow of intellect", {"agi": 8, "dex": 6}, 275, 80,  {"int": 15,  "description": "adds 15 intellect"}, 10],
           ["shortbow of death",     {"agi": 8, "dex": 6}, 275, 80,  {"killing blow": 15, "description": "gives 15% chance for killing blow"}, 10],
           ["shortbow of life",      {"agi": 8, "dex": 6}, 275, 80,  {"health": 100, "description": "gives 100 hp"}, 10],
           ["shortbow of haste",     {"agi": 8, "dex": 6}, 275, 80,   {"crit rate": 15, "description": "adds 15% to crit rate"}, 10],
           ["composite bow", {"agi": 10, "dex": 6}, 300, 100, 10],
           ["composite bow of strength",  {"agi": 10, "dex": 6}, 500, 100,  {"str": 15, "description": "adds 15 strength"}, 5],
           ["composite bow of dexterity", {"agi": 10, "dex": 6}, 500, 100,  {"dex": 15,  "description": "adds 15 dex"}, 5],
           ["composite bow of agility",   {"agi": 10, "dex": 6}, 500, 100,  {"agi": 15,  "description": "adds 15 agility"}, 5],
           ["composite bow of intellect", {"agi": 10, "dex": 6}, 500, 100,  {"int": 15,  "description": "adds 15 intellect"}, 5],
           ["composite bow of death",     {"agi": 10, "dex": 6}, 500, 100,  {"killing blow": 15, "description": "gives 15% chance for killing blow"}, 5],
           ["composite bow of life",      {"agi": 10, "dex": 6}, 500, 100,  {"health": 100, "description": "gives 100 hp"}, 5],
           ["composite bow of haste",     {"agi": 10, "dex": 6}, 500, 100,   {"crit rate": 15, "description": "adds 15% to crit rate"}, 5],
           ]


armor = [["cloth armor", {"armor": 100, "dex": 15}, 100, 50], ["leather armor", {"armor": 110, "dex": 12}, 200, 40],
         ["copper armor", {"armor": 130, "dex": 10}, 500, 30], ["iron armor", {"armor": 170, "dex": 8}, 1000, 20],
         ["steel armor", {"armor": 200, "dex": 5}, 1500, 10],]

accessories = [["small shield", {"armor": 50}, 100, "arm", 40], ["medium shield", {"armor": 100}, 200, "arm", 30],
               ["heavy shield", {"armor": 150}, 400, "arm", 20],
               ["copper ring", {"crit rate": 2, "killing blow": 2}, 20, "finger", 50],
               ["gold ring", {"crit rate": 5, "killing blow": 5}, 750, "finger", 40 ],
               ["platinum ring", {"crit rate": 7, "killing blow": 10}, 1500, "finger", 5],
               ["iron necklace", {"crit rate": 2}, 50, "neck", 40], ["gold necklace", {"crit rate": 5}, 100, "neck", 40],
               ["platinum necklace", {"crit rate": 7}, 1000,  "neck", 10],
               ]

heal = [["apple", 5, 10, 60], ["bread", 10, 15, 60], ["chicken", 15, 20, 50], ["minor health potion", 50, 50, 40],
        ["medium health potion", 75, 75, 35], ["major health potion", 100, 100, 30], ["master health potion", 100, 100, 20]]


misc = [["lesser strength gem", {"str": 5}, 30, 30], ["medium strength gem", {"str": 10}, 20, 20], ["major strength gem", {"str": 15}, 10, 10],
        ["lesser dexterity gem", {"dex": 5}, 30, 30], ["medium dexterity gem", {"dex": 10}, 20, 20], ["major dexterity gem", {"dex": 15}, 10, 10],
        ["lesser agility gem", {"agi": 5}, 30, 30], ["medium agility gem", {"agi": 10}, 20, 20], ["major agility gem", {"agi": 15}, 10, 10],
        ["lesser intellect gem", {"int": 5}, 30, 30], ["medium intellect gem", {"int": 10}, 20, 20], ["major intellect gem", {"int": 15}, 10, 10],
        ["copper ore", {}, 0, 25], ["iron", {}, 0, 25], ["steel", {},  0, 20],
        ["oak wood", {}, 0, 25], ["alder wood", {},  0, 25], ["hickory", {},  0, 25],
        ["weapon upgrade", "weapon upgrade", 5, 15], ["armor upgrade", "armor upgrade",5, 15], ["accessory upgrade", "accessory upgrade", 5, 15]
        ]

weaponsdict = {}
armordict = {}
healthitems = {}
accdict = {}
miscdict = {}
for item in weapons:
    if len(item) < 6:
        weaponsdict[item[0]] = Items(item[0], attributes=item[1], price=item[2], type="weapon", power=item[3], droprate=item[4])
    else:
        weaponsdict[item[0]] = Items(item[0], attributes=item[1], price=item[2], type="weapon", power=item[3], weapon_ability=item[4], droprate=item[5])

for item in armor:
    armordict[item[0]] = Items(item[0], attributes=item[1], price=item[2], type="armor", droprate=item[3])

for item in heal:
    healthitems[item[0]] = Items(item[0], price=item[1], health=item[2], type="heal", droprate=item[3])

for item in misc:
    if "upgrade" in item[0]:
        miscdict[item[0]] = Items(name=item[0], ability=item[1], droprate=item[3])
    else:
        miscdict[item[0]] = Items(name=item[0], attributes=(item[1]),  droprate=item[3])

for item in accessories:
    accdict[item[0]] = Items(name=item[0], attributes=item[1], price=item[2], slot=item[3], droprate=item[4])

