import os

def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == "R":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == "L":
        smer = smeri[(ismer - 1) % 4]
    else:
        dx, dy = premiki[ismer]
        x += dx * ukaz
        y += dy * ukaz
    return x, y, smer
'''
def izvedi(ime_datoteke):
    with open(ime_datoteke, "r") as f:
        r = f.read().splitlines()
        return lambda x, y, smer: [x, y, smer = premik(x, y, smer) for ukaz in r] 
'''

"""def izvedi(ime_datoteke):
    directions = "NESW"
    c_state = "N"
    c_coords = (0, 0)
    container = []
    container.append((0,0, c_state))
    with open(ime_datoteke, "r") as f:
        s = f.read()
    s = s.split("\n")
    if '' in s:
        s.remove('')
    for item in s:
        x, y = c_coords
        if item == "DESNO":
            if c_state == "W":
                c_state = "N"
            else:
                c_state = directions[directions.index(c_state)+1]
        if item == "LEVO":
            if c_state == "N":
                c_state = "W"
            else:
                c_state = directions[directions.index(c_state) - 1]
        elif "NAPREJ" in item:
            a = item.split(" ")
            if c_state == "N":
                y -= int(a[1])
            elif c_state == "S":
                y += int(a[1])
            elif c_state == "W":
                x -= int(a[1])
            elif c_state == "E":
                x += int(a[1])
            c_coords = (x, y)
        container.append((x, y, c_state))
    return container
"""

'''def izvedi(ime_datoteke):
    container = []
    x = y = 0
    smer = "N"
    container.append((x,y, smer))
    datoteka = open(ime_datoteke, "r", encoding="utf-8")
    lines = datoteka.read().splitlines()
    for i in lines:
        x = int(x)
        y = int(y)
        if "DESNO" in i:
            current = premik("R", x, y, smer)
        elif "LEVO" in i:
            current = premik("L", x, y, smer)
        elif "NAPREJ" in i:
            n = i.split(" ")[1]
            current = premik(int(n), x, y, smer)
        x, y, smer = current
        container.append(current)
    return container'''

'''
def izvedi(ime_datoteke):
    container = []
    x = y = 0
    smer = "N"
    container.append((x,y, smer))
    datoteka = open(ime_datoteke, "r", encoding="utf-8")
    lines = datoteka.read().splitlines()
    for i in lines:
        x = int(x)
        y = int(y)
        if "DESNO" in i:
            current = premik("R", x, y, smer)
        elif "LEVO" in i:
            current = premik("L", x, y, smer)
        elif "NAPREJ" in i:
            n = i.split(" ")[1]

            line_split = line.split(" ")
            current = premik(int(n), x, y, smer)
        x, y, smer = current
        container.append(current)
    return container


'''

'''def izvedi(ime_datoteke):
    with open(ime_datoteke, "r") as f:
        navodila = f.read().splitlines()
    seznam = []
    n = ""
    smer = "N"
    x = 0
    y = 0
    seznam.append((x,y,smer))
    for navodilo in navodila:
        if navodilo == "DESNO":
            n = "R"
        elif navodilo == "LEVO":
            n = "L"
        elif navodilo[:6] == "NAPREJ":
            navodilo_split = navodilo.split(" ")
            n = int(navodilo_split[1])
        x,y,smer = premik(n, x, y, smer)
        seznam.append((x, y, smer))
    return seznam


'''
#print(izvedi("primer.txt"))



'''
znak = "^"
smeri = [["N", "^"], ["S", "v"], ["W", "<"], ["E", ">"]]
for sm, zn in smeri: 
    if sm == smer: 
        znak = zn

'''


import unittest


class TestObvezna(unittest.TestCase):

    def test_branje(self):
        self.assertEqual(
            izvedi("primer.txt"),
            [(0, 0, 'N'), (0, 0, 'E'), (12, 0, 'E'), (12, 0, 'S'), (12, 2, 'S'),
             (12, 2, 'E'), (15, 2, 'E'), (15, 2, 'N'), (15, 2, 'W')]
        )
        self.assertEqual(
            izvedi("ukazi.txt"),
            [(0, 0, 'N'), (0, 0, 'E'), (1, 0, 'E'), (1, 0, 'S'), (1, 0, 'W'),
             (0, 0, 'W'), (0, 0, 'S'), (0, 0, 'E'), (1, 0, 'E'), (1, 0, 'S'),
             (1, 3, 'S'), (1, 3, 'E'), (2, 3, 'E'), (2, 3, 'S'), (2, 3, 'W')]
        )

'''
    def test_opisi_stanje(self):
        self.assertEqual(opisi_stanje(0, 12, "N"), "  0:12  ^")
        self.assertEqual(opisi_stanje(111, 0, "E"), "111:0   >")
        self.assertEqual(opisi_stanje(-2, 111, "S"), " -2:111 v")
        self.assertEqual(opisi_stanje(0, 0, "W"), "  0:0   <")


    def test_prevedi(self):
        from random import randint
        import os
        ime = "izhod{:05}.txt".format(randint(0, 99999))
        try:
            self.assertIsNone(prevedi("primer.txt", ime))
            self.assertEqual(open(ime).read().rstrip(), """  0:0   ^
  0:0   >
 12:0   >
 12:0   v
 12:2   v
 12:2   >
 15:2   >
 15:2   ^
 15:2   <""")

            self.assertIsNone(prevedi("ukazi.txt", ime))
            self.assertEqual(open(ime).read().rstrip(), """  0:0   ^
  0:0   >
  1:0   >
  1:0   v
  1:0   <
  0:0   <
  0:0   v
  0:0   >
  1:0   >
  1:0   v
  1:3   v
  1:3   >
  2:3   >
  2:3   v
  2:3   <""")
        finally:
            os.remove(ime)

        vime = "vhod{:05}.txt".format(randint(0, 99999))
        open(vime, "wt").write("NAPREJ 23\nLEVO\nNAPREJ 17\n")
        try:
            self.assertIsNone(prevedi(vime, ime))
            self.assertEqual(open(ime).read().rstrip(), """  0:0   ^
  0:-23 ^
  0:-23 <
-17:-23 <""")
        finally:
            os.remove(ime)
            os.remove(vime)


class TestDodatna(unittest.TestCase):
    def test_opisi_stanje(self):
        self.assertEqual(opisi_stanje_2(0, 12, "N"),   "^   (0:12)")
        self.assertEqual(opisi_stanje_2(111, 0, "E"),  "> (111:0)")
        self.assertEqual(opisi_stanje_2(-2, 111, "S"), "v  (-2:111)")
        self.assertEqual(opisi_stanje_2(0, 0, "W"),    "<   (0:0)")

'''

if __name__ == "__main__":
    unittest.main()
