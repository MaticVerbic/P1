# 8. domača naloga
'''
import csv
def preberi_podatke(pot):
    with open(pot, newline = '', encoding = "utf-8") as f:
        vrednosti = []
        s = dict()
        resitev = dict()
        r = csv.reader(f, delimiter=" ")
    
        for line in r:
            vrednosti.append(line)

        kraji = " ".join(vrednosti[0]).split(';')[1:]
    

        for dan in range(1, len(vrednosti)):
            po_dnevih = vrednosti[dan]
            loceno_po_dnevih = po_dnevih[0].split(';')[1:]
            for i in range(0, len(loceno_po_dnevih)):
                if loceno_po_dnevih[i] != '':
                    s[kraji[i]] = int(loceno_po_dnevih[i])
            resitev[dan] = s

    return resitev
            
print(preberi_podatke('februar.csv'))
'''
import csv

def preberi_podatke(filename):
    slovar = {}
    with open(filename, "r", encoding="utf-8") as f:
        r = csv.reader(f, delimiter=" ")
        values = []
        for row in r:
            values.append(row)
    kraji = " ".join(values[0]).split(";")[1:]
    vrednosti_brez_dneva = []
    for line in values[1:]:
        if isinstance(line, list):
            vrednosti_brez_dneva.append(line[0].split(";")[1:])
            slovar[int(line[0].split(";")[0])] = {}
        else:
            vrednosti_brez_dneva.append(line.split(";")[1:])
            slovar[int(line.split(";")[0])] = {}
    print(vrednosti_brez_dneva)
    for item in slovar:
        for kraj in kraji:
            slovar[item][kraj] = 0

    for sl, values in zip(slovar, vrednosti_brez_dneva):
        for item, val in zip(slovar[sl], values):
            if val == '':
                continue
            slovar[sl][item] = val
    for item in slovar:
        new_dict = {}
        for key, value in slovar[item].items():
            if value != 0:
                new_dict[key] = int(value)
        slovar[item] = new_dict

    return slovar
'''
import csv

def preberi_podatke(filename):
    slovar = {}
    with open(filename, "r", encoding="utf-8") as f:
        r = csv.reader(f, delimiter=" ")
        values = []
        for row in r:
            values.append(row)
    kraji = " ".join(values[0]).split(";")[1:]
    vrednosti_brez_dneva = []
    for line in values[1:]:
        if isinstance(line, list):
            vrednosti_brez_dneva.append(line[0].split(";")[1:])
            slovar[int(line[0].split(";")[0])] = {}
        else:
            vrednosti_brez_dneva.append(line.split(";")[1:])
            slovar[int(line.split(";")[0])] = {}

    for item in slovar:
        for kraj in kraji:
            slovar[item][kraj] = 0

    for sl, values in zip(slovar, vrednosti_brez_dneva):
        for item, val in zip(slovar[sl], values):
            if val == '':
                continue
            slovar[sl][item] = val

    for item in slovar:
        new_dict = {}
        for key, value in slovar[item].items():
            if value != 0:
                new_dict[key] = value
        slovar[item] = new_dict


    return slovar

'''
