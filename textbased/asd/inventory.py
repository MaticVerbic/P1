class Items:
    def __init__(self, name, attributes = "", price=0, health=0):
        self.name = name
        self.attributes = attributes
        self.price = price
        self.health = health

weapons = [["copper sword", {"str": 2, "dex": 1}, 50], ["iron sword", {"str": 4, "dex": 2}, 100],
           ["steel sword", {"str": 6, "dex": 4}, 200], ["expert sword", {"str": 15, "dex": 10}, 1000],
           ["master sword", {"str": 10, "dex": 8}, 500], ["basic bow", {"agi": 2, "dex": 2}, 20],
           ["homemade bow", {"agi": 4, "dex": 2}, 50], ["longbow", {"agi": 8, "dex": 4}, 100],
           ["shortbow", {"agi": 8, "dex": 6}, 100], ["composite bow", {"agi": 10, "dex": 6}, 300],]
armor = [["cloth armor", {"armor": 100, "dex": 15}, 100], ["leather armor", {"armor": 110, "dex": 12}, 200],
         ["copper armor", {"armor": 130, "dex": 10}, 500], ["iron armor", {"armor": 170, "dex": 8}, 1000],
         ["steel armor", {"armor": 200, "dex": 5}, 1500],]

heal = [["apple", 5, 10], ["bread", 10, 15], ["chicken", 15, 20], ["minor health potion", 50, 50],
        ["medium health potion", 75, 75], ["major health potion", 100, 100], ["master health potion", 100, 100]]
weaponsdict = {}
armordict = {}
healthitems = {}
for item in weapons:
    weaponsdict[item[0]] = Items(item[0], item[1], item[2])

for item in armor:
    armordict[item[0]] = Items(item[0], item[1], item[2])

for item in heal:
    healthitems[item[0]] = Items(item[0], price=item[1], health=item[2])

