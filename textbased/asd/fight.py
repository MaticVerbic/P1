class Fight:
    def __init__(self, p, e):
        self.p = p
        self.e = e


    def calc_enemy_str(self):
        return int(((self.e.level + self.e.experience)/2))

    def calc_player_str(self):
        power = 0
        if self.p.equipped_weapon != "":
            w = self.p.weapons[self.p.equipped_weapon.lower()]
            for i in w.attributes.values():
                power += i
        power += self.p.str
        power += self.p.agi
        return power

    def calc_player_arm(self):
        arm = 0
        if self.p.equipped_armor != "":
            ar = self.p.armor[self.p.equipped_armor.lower()].attributes["armor"]
            arm += ar
        arm += self.p.stamina
        arm /= 1.5
        return int(arm)

    def fight_calc(self):
        estr = self.calc_enemy_str()
        pstr = self.calc_player_str()
        parm = self.calc_player_arm()
        enemy_hits = int(estr/pstr)
        if enemy_hits < 1:
            return True
        else:
            p_hits = int(parm/estr)
            self.p.health -= int(p_hits*5)
            if self.p.health <= 0:
                return False
            else:
                return True

    def fight_c(self):
        if self.fight_calc():
            self.p.add_xp(self.e.experience)
            return True
        else:
            return False