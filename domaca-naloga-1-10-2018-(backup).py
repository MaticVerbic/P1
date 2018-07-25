import risar
from random import randint, random
from PyQt5.QtWidgets import QMessageBox
import time
risar.obnavljaj = True


'''class Krog:
    def __init__(self, polmer, sirina, hx=0, hy=0):
        self.x = randint(35, risar.maxX-55)
        self.hx = hx
        self.y = randint(35, risar.maxY-55)
        self.hy = hy
        self.polmer = polmer
        self.sirina = sirina
        self.barva = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))
        self.risi = risar.krog(self.x, self.y, self.polmer, self.barva, self.sirina)
        self.risi.setBrush(self.risi.pen().color().lighter())'''


'''krog = risar.krog(randint(35, risar.maxX-55), randint(35, risar.maxY-55), 30,
                  risar.barva(randint(0, 255), randint(0, 255), randint(0, 255)), 10)
hx = 2* random() + 3
hy = 2* random() + 3
for i in range(1000):
    krog.setPos(krog.x() + hx, krog.y() + hy)
    if not (35 < krog.x() < risar.maxX - 35):
        hx = -hx
    if not (35 < krog.y() < risar.maxY - 35):
        hy = -hy
    risar.cakaj(0.02)
    
    #krog.setBrush(krog.pen().color().lighter())
    
    '''



def pobarvaj(item, alpha):
    color = item.pen().color().lighter()
    color.setAlpha(alpha)
    item.setBrush(color)


def za_6():
    krog = risar.krog(randint(15, risar.maxX - 15), randint(15, risar.maxY - 15), 10,
                      risar.barva(randint(0, 255), randint(0, 255), randint(0, 255)), 3)
    x, y = 2 * random() + 3, 2 * random() + 3
    t = time.time()
    for i in range(1000):
        if time.time()-t > 20:
            exit()
        krog.setPos(krog.x() + x, krog.y() + y)
        if not (15 < krog.x() < risar.maxX-15):
            x = -x
        if not (15 < krog.y() < risar.maxY-15):
            y = -y
        risar.cakaj(0.02)

def za_7():
    krogi = []
    for i in range(30):
        krog = risar.krog(randint(15, risar.maxX-15), randint(15, risar.maxY-15), 10,
                      risar.barva(randint(0, 255), randint(0, 255), randint(0, 255)), 3)
        krogi.append([krog, 2* random() + 3, 2* random() + 3])
    t = time.time()
    for i in range(1000):

        for i in range(1000):
            if time.time() - t > 20:
                exit()
        for n in range(len(krogi)):
            item, new_x, new_y = krogi[n]
            item.setPos(item.x() + new_x, item.y() + new_y)
            if not (15 < item.x() < risar.maxX-15):
                krogi[n][1] = -new_x
                #risar.barvaOzadja(risar.barva(randint(0, 255), randint(0, 255), randint(0, 255)))
            if not (15 < item.y() < risar.maxY-15):
                #risar.barvaOzadja(risar.barva(randint(0, 255), randint(0, 255), randint(0, 255)))
                krogi[n][2] = -new_y

        risar.cakaj(0.02)

def za_8():
    krogi = []
    for i in range(30):
        krog = risar.krog(randint(15, risar.maxX - 15), randint(15, risar.maxY - 15), 10,
                          risar.barva(randint(0, 150), randint(0, 150), randint(0, 150)), 3)
        krogi.append([krog, 2 * random() + 3, 2 * random() + 3])
    miska = risar.krog(risar.miska[0], risar.miska[1], 30,
               risar.barva(255, 255, 255), 3)
    for i in range(1000):
        if not risar.klik:
            checkx, checky = risar.miska
            miska.setPos(checkx, checky)
        for n in range(len(krogi)):
            item, new_x, new_y = krogi[n]
            item.setPos(item.x() + new_x, item.y() + new_y)
            if checkx-33 < item.x() < checkx+33 \
                    and checky-33 < item.y() < checky+33 and risar.klik:
                     exit()
            if not (15 < item.x() < risar.maxX - 15):
                krogi[n][1] = -new_x
                #risar.barvaOzadja(risar.barva(randint(0, 255), randint(0, 255), randint(0, 255)))
            if not (15 < item.y() < risar.maxY - 15):
                #risar.barvaOzadja(risar.barva(randint(0, 255), randint(0, 255), randint(0, 255)))
                krogi[n][2] = -new_y

        risar.cakaj(0.02)


def create_circles(stevilo):
    krogi = []
    for i in range(stevilo):
        krog = risar.krog(randint(30, risar.maxX - 30), randint(30, risar.maxY - 30), 10,
                          risar.barva(randint(0, 150), randint(0, 150), randint(0, 150)), 3)
        krogi.append([krog, 2 * random() + 3, 2 * random() + 3, 0, 0, False])
    return krogi


'''def za_9():
    krogi = create_circles()
    miska = risar.krog(risar.miska[0], risar.miska[1], 30,
                       risar.barva(255, 255, 255), 3)

    alive = 1
    stop_koordinate = {(risar.miska[0], risar.miska[1])}
    miska_clock = 0
    checkx, checky = risar.miska
    for i in range(5000):
        if not risar.klik:
            stop_koordinate.remove((checkx, checky))
            checkx, checky = risar.miska
            stop_koordinate.add((checkx, checky))
            miska.setPos(checkx, checky)
        elif time.clock()-miska_clock > 4:
            miska.hide()
            #stop_koordinate.remove((checkx, checky))
        for n in range(len(krogi)):
            item, new_x, new_y, count, stopindeks = krogi[n]
            if time.clock()-count >= 2 and stopindeks:
                print("hidden")
                item.hide()
                stop_koordinate.remove(krogi[n][4])


            elif stopindeks:
                continue
            item.setPos(item.x() + new_x, item.y() + new_y)
            for x, y in stop_koordinate:

                if  x-35.0 < item.x() < x+35.0 and y-35.0 < item.y() < y+33.0 and risar.klik:
                    item.setRect(-30, -30, 60, 60)
                    item.setBrush(item.pen().color().lighter())
                    stop_koordinate.add((item.x(), item.y()))
                    krogi[n][3] = time.clock()
                    miska_clock = time.clock()
                    krogi[n][4] = (item.x(), item.y())
                    alive += 1
                    break
            if not (15 < item.x() < risar.maxX - 15):
                krogi[n][1] = -new_x
            if not (15 < item.y() < risar.maxY - 15):
                krogi[n][2] = -new_y


        risar.cakaj(0.02)'''



def za_9():
    st = time.clock()
    krogi = create_circles(30)

    miska = risar.krog(risar.miska[0], risar.miska[1], 30,
                       risar.barva(255, 255, 255), 3)

    miska_start = 0
    miska_klik = False
    stevec = 0
    stop_koordinate = {"miska": (risar.miska[0], risar.miska[1])}
    for s in range(1000):
        if not risar.klik:
            stop_koordinate["miska"] = (risar.miska[0], risar.miska[1])
            miska.setPos(risar.miska[0], risar.miska[1])

        for n in range(len(krogi)):
            item, new_x, new_y, count, startime, status = krogi[n]
            if time.time()-miska_start >= 4 and miska_klik:
                miska.hide()
                miska_klik = False
                del stop_koordinate["miska"]
                if len(stop_koordinate) == 0:
                    QMessageBox.information(None, "How u doin", str(stevec))
                    exit()
            if startime != 0 and time.time() - krogi[n][4] >= 4:
                item.hide()
                krogi[n][4] = 0
                del stop_koordinate[item]
                if len(stop_koordinate) == 0:
                    QMessageBox.information(None, "How u doin", str(stevec))
                    exit()
                continue

            elif status == True:
                continue
            item.setPos(item.x() + new_x, item.y() + new_y)
            if risar.klik and miska_start == 0:
                pobarvaj(miska, 150)
                '''color = miska.pen().color().lighter()
                color.setAlpha(150)
                miska.setBrush(color)'''
                miska_start = time.time()
                miska_klik = True
            for x, y in stop_koordinate.values():
                if x - 35.0 < item.x() < x + 35.0 and y - 35.0 < item.y() < y + 33.0 and risar.klik:
                        item.setRect(-30, -30, 60, 60)
                        '''color = item.pen().color().lighter()
                        color.setAlpha(randint(120, 180))
                        item.setBrush(color)'''
                        pobarvaj(item,randint(120, 180))
                        stop_koordinate[item] = (item.x(), item.y())
                        krogi[n][4] = time.time()

                        krogi[n][5] = True
                        stevec += 1
                        break

            if not (15 < item.x() < risar.maxX - 15):
                krogi[n][1] = -new_x
            if not (15 < item.y() < risar.maxY - 15):
                krogi[n][2] = -new_y
        risar.cakaj(0.02)
        if time.clock()-st > 20:
            break


def za_10_game(krogov):
    st = time.clock()

    krogi = create_circles(krogov)

    miska = risar.krog(risar.miska[0], risar.miska[1], 30,
                       risar.barva(255, 255, 255), 3)

    miska_start = 0
    miska_klik = False
    stevec = 0
    stop_koordinate = {"miska": (risar.miska[0], risar.miska[1])}
    for s in range(1000):
        if not risar.klik:
            stop_koordinate["miska"] = (risar.miska[0], risar.miska[1])
            miska.setPos(risar.miska[0], risar.miska[1])

        for n in range(len(krogi)):
            item, new_x, new_y, count, startime, status = krogi[n]
            if time.time()-miska_start >= 4 and miska_klik:
                miska.hide()
                miska_klik = False
                del stop_koordinate["miska"]
                if len(stop_koordinate) == 0:
                    return stevec
            if startime != 0 and time.time() - krogi[n][4] >= 4:
                item.hide()
                krogi[n][4] = 0
                del stop_koordinate[item]
                if len(stop_koordinate) == 0:
                    return stevec
                continue

            elif status == True:
                continue
            item.setPos(item.x() + new_x, item.y() + new_y)
            if risar.klik and miska_start == 0:
                pobarvaj(miska, 150)
                '''color = miska.pen().color().lighter()
                color.setAlpha(150)
                miska.setBrush(color)'''
                miska_start = time.time()
                miska_klik = True
            for x, y in stop_koordinate.values():
                if x - 35.0 < item.x() < x + 35.0 and y - 35.0 < item.y() < y + 33.0 and risar.klik:
                        item.setRect(-30, -30, 60, 60)
                        '''color = item.pen().color().lighter()
                        color.setAlpha(randint(120, 180))
                        item.setBrush(color)'''
                        pobarvaj(item,randint(120, 180))
                        stop_koordinate[item] = (item.x(), item.y())
                        krogi[n][4] = time.time()

                        krogi[n][5] = True
                        stevec += 1
                        break

            if not (15 < item.x() < risar.maxX - 15):
                krogi[n][1] = -new_x
            if not (15 < item.y() < risar.maxY - 15):
                krogi[n][2] = -new_y
        risar.cakaj(0.02)
        if time.clock()-st > 20:
            break
    return stevec


def za_10():
    pravila = [(1, 8), (2, 10), (4, 12), (8, 16), (12, 20), (16, 24), (20, 28), (25, 30), (28, 30), (30, 30)]
    for potrebnih, vseh in pravila:
        risar.klik = False
        QMessageBox.information(None, "Nivo {}".format(pravila.index((potrebnih, vseh))+1),
                                "Potrebujete zadeti {} od {}.".format(potrebnih, vseh))
        rezultat = za_10_game(vseh)
        if potrebnih <= rezultat:
            QMessageBox.information(None, "Nivo {}".format(pravila.index((potrebnih, vseh))+1),
                                    "Zadeli ste {} od {} zog. Zmaga!".format(rezultat, vseh))
        else:
            QMessageBox.information(None, "Nivo {}".format(pravila.index((potrebnih, vseh))+1),
                                    "Zadeli ste {} od {} zog. Konec!".format(rezultat, vseh))
        risar.pobrisi()
    print("exiting for no reason at all")



#za_6()
#za_7()
#za_8()
#za_9()
za_10()


