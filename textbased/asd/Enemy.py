from random import randint
class Enemy:
    def __init__(self, name, level, experience):
        self.name = name
        self.level = level
        self.experience = experience



hum = ["Barbarian", "Soldier", "Thief", "Wizard", "John Cena"]
ani = ["Bear", "Snake", "Wolf", "Boar"]
mag = ["Abomination", "Banshee", "Basilisk", "Brownies", "Centaur", "Cyclops", "Dragon", "Drake",
       "Dwarfs", "Elves", "Ettans", "Faeries", "Giants", "Ghost", "Gnome", "Goblin", "Golem",
       "Griffin", "Grim Reaper", "Ghoul", "Gnolls", "Harpies", "Kobold", "Leprechaun"]

humdict = {}
anidict = {}
magdict = {}
for h in hum:
    humdict[h] = Enemy(h, randint(5, 15), randint(20, 80))

for a in ani:
    anidict[a] = Enemy(a, randint(1, 5), randint(10, 20))

for m in mag:
    magdict[m] = Enemy(m, randint(10, 30), randint(30, 120))

"""for h in humdict:
    print(vars(humdict[h]))

for a in anidict:
    print(vars(anidict[a]))

for m in magdict:
    print(vars(magdict[m]))"""