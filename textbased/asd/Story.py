from inventory import *
from fight import *
from Enemy import *

class Story:
    def __init__(self, p):
        self.p = p

    def greeting(self):
        s = 'Your name is ' + self.p.name + ', you\'re a viking from Sweden! You set of on a journey to find riches!'
        return s

    def character(self, inp):
        if inp == "i":
            self.p.print_inv()
            self.lines("l")


    def lines(self, ar):
        if ar == "n":
            print("\n---Notice---\n")

        elif ar == "t":
            print("\n---Tips---\n")

        elif ar == "l":
            print("\n------\n")



    def chap1(self):
        s = "You're awoken from sleep by a hot flash and loud screams. \nYour house has been set on fire by a rival clan. "
        s += "\nYou quickly gather items closest to yourself, a copper sword, some clothes, an apple and a loaf of bread"
        self.p.app_weapons(weaponsdict["copper sword"])
        self.p.app_armor(armordict["cloth armor"])
        self.p.equip_weapon(self.p.weapons["copper sword"])
        self.p.equip_armor(self.p.armor["cloth armor"])
        self.p.app_health(healthitems["apple"])
        self.p.app_health(healthitems["bread"])
        self.p.add_gold(100)
        s += "\nYou manage to escape the burning building through the window and hide in nearby forest without anyone seeing you. "
        print(s)
        self.lines("n")
        notice = "Copper sword, cloth armor, apple, bread and 100 golden coins added to inventory. To see inventory enter I at any prompt"
        print(notice)
        self.lines("t")
        inp =  input("To view your inventory enter i otherwise enter anything else\n").lower()
        self.character(inp)
        s = "As the raid is over, you leave your cover. Your village is destroyed and everyone is dead. "
        s += "There is nothing left for you in this village, so you decide to leave in search of riches. \nYou decide to go east, to Miklagard. "
        s += "\nBut you decide to head to your friends in a village north of you to ask for help. "
        s += "\n\nAs you walk down the forest path the following day, you hear a rustle in the bushes. It's a giant boar!"
        print(s)
        self.lines("t")
        t = "When you enter a fight, you have 3 options. \n1. To fight enter 1, 2. To flee enter 2 and 3. To hide enter 3. \n"
        t += "If you fight, you might die, if you choose to hide the enemy might find you and force you into a fight." \
             "\nAnytime there's a prompt you can enter c to enter character screen."
        print(t)
        self.lines("l")
        inp = input("What is your choice?\n").lower()
        if inp == "c":
            self.p.print_stats()
            inin = input("Do you wish to view your inventory?\n")
            self.character(inin)
        elif inp == "1":
            f = Fight(self.p, anidict["Bear"])
            if f.fight_c():
                self.p.add_xp(anidict["Bear"].experience)
                self.lines("n")
                print(anidict["Bear"].experience, "experience gained! Your HP after the fight is: %s" % (self.p.health))
                self.lines("l")
                print("You won! You take some time to rest and continue on your way!")
            else:
                print("You lost the fight, sorry. Bye")
                exit()
