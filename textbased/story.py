from textbased.inventory import *
from textbased.fight import *
from textbased.enemy import *
from textbased.save_load import *

class Story:
    def __init__(self, p, v, t):
        self.p = p
        self.current_chapter = 0
        self.v = v
        self.t = t
        self.sl = Save_load(self.p, self.v)

    def greeting(self):
        s = 'Your name is ' + self.p.name + ', you\'re a viking from Sweden! You set of on a journey to find riches!'
        return s

    def call_char(self, inp):
        if inp == "c":
            self.p.print_stats()
            inp = input("Do you wish to view your inventory? [y/n]\n")
            if inp.lower() != "y":
                return
            else:
                self.character()

    def call_save(self):
        self.sl.get_current_chap(self.current_chapter)
        print(self.sl.current_chapter, self.current_chapter)
        self.sl.save()
        return

    def character(self):
        self.p.print_inv()
        self.lines("l")
        self.p.print_stats()
        if self.p.calc_level():
            inp = input("You seem to have leveled up, do you wish to distribute skill points? [y/n]\n")
            if inp == "y":
                self.p.player_choice_stats()
        inp = input("Do you wish to use an item? [y/n] \n")
        if inp == "y":
            inp = input("To equip armor/weapon, enter equip, to remove armor/weapon enter"
                        " remove, to use a potion, enter potion \n")
            if inp == "equip" or inp == "e":
                inp = input("Weapon or armor?\n")
                if inp == "weapon" or inp == "w":
                    inp = input("Weapon name?\n")
                    for item in weaponsdict.values():
                        if inp.lower() == item.name:
                            self.p.equip_weapon(item)
                elif inp == "armor" or inp == "a":
                    inp = input("Armor name?\n")
                    for item in armordict.values():
                        if inp.lower() == item.name:
                            self.p.equip_armor(item)
            elif inp == "remove":
                ...
            elif inp == "potion":
                inp = input("Item name? \n")
                for i in self.p.healthitems:
                    if inp.lower() == i.name:
                        self.p.use_health(i.health)
                        del i


        elif inp == "n":
            return False

    def lines(self, ar):
        if ar == "n":
            print("\n---Notice---")

        elif ar == "t":
            print("\n---Tips---")

        elif ar == "l":
            print("\n------")

    def call_choice(self, inputs, inp, question="What is your choice?\n"):
        while inp not in inputs:
            if inp == "c":
                self.call_char(inp)
            elif inp == "s":
                self.call_save()
            inp = input(question).lower()
        return inp



    def chap0(self):
        self.current_chapter = 0
        s = "You're awoken from sleep by a hot flash and loud screams. \nYour house has been set on fire by a rival clan. "
        s += "\nYou quickly gather items closest to yourself, a copper sword, some clothes, an apple and a loaf of bread"
        self.p.app_weapons(weaponsdict["copper sword"])
        self.p.app_armor(armordict["cloth armor"])
        self.p.equip_weapon(self.p.weapons["copper sword"])
        self.p.equip_armor(self.p.armor["cloth armor"])
        self.p.app_health(healthitems["apple"],1)
        self.p.app_health(healthitems["bread"],1)
        self.p.add_gold(100)
        s += "\nYou manage to escape the burning building through the window and hide in nearby forest without anyone seeing you. "
        print(s)
        self.lines("n")
        notice = "Copper sword, cloth armor, apple, bread and 100 golden coins added to inventory. To see inventory enter c at any prompt"
        print(notice)
        self.lines("t")
        inp =  input("To view your inventory enter i otherwise enter anything else\n").lower()
        if inp == "i":
            self.p.print_inv()
            self.p.equip_weapon(weaponsdict["copper sword"])
            self.p.equip_armor(armordict["cloth armor"])
    def chap1(self):
        self.current_chapter = 1

        s = "As the raid is over, you leave your cover. Your village is destroyed and everyone is dead. "
        s += "There is nothing left for you in this village, so you decide to leave in search of riches. \nYou decide to go east, to Miklagard. "
        s += "\nBut you decide to head to your friends in a village north of you to ask for help. "
        s += "\n\nAs you walk down the forest path the following day, you hear a rustle in the bushes. It's a giant boar!"
        print(s)
        self.lines("t")
        t = "When you enter a fight, you have 3 options. \n1. To fight enter 1, 2. To flee enter 2 and 3. To hide enter 3. \n"
        t += "If you fight, you might die, if you choose to hide the enemy might find you and force you into a fight." \
             "\nAnytime there's a prompt you can enter c to enter character screen or s to save the game."
        print(t)
        self.lines("l")
        inp = input("What is your choice?\n").lower()
        inps = ["1", "2", "3"]
        inp = self.call_choice(inps, inp)
        if inp == "1":
            f = Fight(self.p, anidict["Boar"])
            if f.fight_c():
                self.p.add_xp(anidict["Boar"].experience)
                self.lines("n")
                print(anidict["Boar"].experience, "experience gained! Your HP after the fight is: %s" % (self.p.health))
                self.lines("l")
                print("You won! You take some time to rest and continue on your way!")
            else:
                print("You lost the fight, sorry. Bye")
                exit()

    def chap2(self):
        self.t.quest1()