from math import *

hitrost = float(input("Vnesite hitrost (m/s): "))
kot = radians(float(input("Vnesite kot (°): ")))
rezultat = (hitrost**2 * sin(2*kot)) / 9.81

print("Kroglo bo odneslo %sm dalec. " % (rezultat) )

input("Press enter to exit. ")