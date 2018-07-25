from random import randint


def osnovno():
    # Obvezna naloga
    ana = 1
    berta = 1

    while (ana < 30 and berta < 30 ):
        countana = randint(1, 6)
        countberta = randint(1, 6)
        ana += countana
        berta += countberta
        if(ana >= 30):
            print("Ana vrže %s in zmaga z %s tock. " % (countana, ana))
        elif(berta >= 30):
            print("Ana vrže %s in zmaga z %s tock. " % (countana, ana))
            print("Berta vrže %s in zmaga z %s tock. " % (countberta, berta))
        else:
            print("Ana vrže %s in je na polju %s" % (countana, ana))
            print("Berta vrže %s in je na polju %s" % (countberta, berta))


def prvadodatna():
    # prva dodatna naloga
    ana = 1
    berta = 1

    while(ana < 30 and berta < 30):
        cana = randint(1, 6)
        ana += cana
        if (ana >= 30):
            print("Ana vrže %s in zmaga na %s polju. " % (cana, ana))
            break
        elif (ana == berta):
            print("Ana vrže %s in je na polju %s. " % (cana, ana))
            print("Ana požre Berto, ki gre nazaj na polje 1")
            berta = 1
        else:
            print("Ana vrže %s in je na polju %s. " % (cana, ana))
        while(cana == 6):
            cana = randint(1,6)
            ana += cana
            if (ana == berta):
                print("Ana vrže %s in je na polju %s. " % (cana, ana))
                print("Ana požre Berto, ki gre nazaj na polje 1. ")
                berta = 1
            if (ana >= 30):
                print("Ana vrže %s in zmaga na %s polju. " % (cana, ana))
                return
            else:
                print("Ana vrže %s in je na polju %s. " % (cana, ana))
        cber = randint(1, 6)
        berta += cber
        if (berta >= 30):
            print("Berta vrže %s in zmaga na %s polju. " % (cber, berta))
            break
        elif (berta == ana):
            print("berta vrže %s in je na polju %s. " % (cber, berta))
            print("Berta požre Ano, ki gre nazaj na polje 1.")
            ana = 1
        else:
            print("Berta vrže %s in je na polju %s. " % (cber, berta))
        while(cber == 6):
            cber = randint(1,6)
            berta += cber
            if (berta == ana):
                print("Berta vrže %s in je na polju %s. " % (cber, berta))
                print("Berta požre Ano, ki gre nazaj na polje 1.")
                ana = 1
            if (berta >= 30):
                print("berta vrže %s in zmaga na %s polju. " % (cber, berta))
                return
            else:
                print("Berta vrže %s in je na polju %s. " % (cber, berta))



def drugadodatna():
    # druga dodatna naloga
    igralke = [["Ana", 0, 1], ["Berta", 0, 1], ["Cilka", 0, 1], ["Dani", 0, 1], ["Ema", 0, 1], ["Fanči", 0, 1]]
    i = randint(0, 5)
    print("Prva meče", igralke[i][0])
    while igralke[i][2] != 30:
        if igralke[i][2] == 1:
            # če je polje 1
            igralke[i][1] = randint(1, 6)
            if (igralke[i][1] != 6):
                print("%s ni vrgla 6 zato ostane na 1. polju." % (igralke[i][0]))
                i += 1
                if i > 5:
                    i = 0
                continue
        else:
            igralke[i][1] = randint(1, 6)
            if (igralke[i][2] + igralke[i][1]) > 30:
                print("%s je vrgla %s, kar je več kot 30, zato se ne premakne." % (igralke[i][0], igralke[i][1]))
                i += 1
                if i > 5:
                    i = 0
                continue
            else:
                igralke[i][2] += igralke[i][1]
        print("%s vrže %s in je na polju %s." % (igralke[i][0], igralke[i][1], igralke[i][2]))

        for igr in igralke:
            if igralke[i][2] == igr[2] and igr[0] != igralke[i][0] and igralke[i][2] != 1:
                print("%s požre %s, ki gre nazaj na polje 1." % (igralke[i][0], igr[0]))
                igr[2] = 1
        if igralke[i][2] >= 30:
            print(igralke[i][0], "zmaga!")
            break
        while igralke[i][1] == 6:
            # ce je 6 mece ponovno
            igralke[i][1] = randint(1, 6)
            if (igralke[i][2] + igralke[i][1]) > 30:
                print("%s je vrgla %s, kar je več kot 30, zato se ne premakne." % (igralke[i][0], igralke[i][1]))
                break
            else:
                igralke[i][2] += igralke[i][1]
            print("%s vrže %s in je na polju %s." % (igralke[i][0], igralke[i][1], igralke[i][2]))
            for igr in igralke:
                if igralke[i][2] == igr[2] and igr[0] != igralke[i][0] and igralke[i][2] != 1:
                    print("%s požre %s, ki gre nazaj na polje 1." % (igralke[i][0], igr[0]))
                    igr[2] = 1
            if igralke[i][2] >= 30:
                print(igralke[i][0], "zmaga!")
                return



        if igralke[i][2] >= 30:
            print(igralke[i][0], "zmaga!")
            break
        i += 1
        if i >= 5:
            i = 0

print("################\nObvezna Naloga\n################\n\n")
osnovno()
print("\n\n\n###################\nPrva Dodatna Naloga\n###################\n\n")
prvadodatna()
print("\n\n\n###################\nDruga Dodatna Naloga\n###################\n\n")
drugadodatna()

input("Any button to exit...")