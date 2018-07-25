from math import *
from random import randint
def tarca():
    razdalja = float(input("Vnesite razdaljo: "))

    '''
    randkot = randint(10,75)
    rad = radians(randkot)
    hitrost = sqrt((razdalja * 9.81)/ (sin(2*rad)))

    print("v: %s, k: %s, r: %s" % (hitrost, randkot, razdalja))
    
    '''

    guessa = 0
    guessv = 0

    razvne = -1

    while(int(razvne) not in range(int(razdalja)-10, int(razdalja+10))):
        guessa = float(input("Vnesite kot (°): "))
        guessv = float(input("Vnesite hitrost (m/s): "))
        razvne = (guessv**2 * sin(2*radians(guessa))) / 9.81



    print("Od kota ste bili oddaljeni %s metrov" % abs(razdalja - int(razvne)))




tarca()
input("Press any button to exit...")
