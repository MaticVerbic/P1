def prastevilo(stevilo):

    for stev in range(2, int(stevilo/2)):
        if stevilo%stev == 0:
            return False
    else:
        return True

print(prastevilo(43))

def prastevilabetter(n):
    container = [2]
    for stev in range(3, n):
        if stev % 2 == 0:
            continue
        else:
            container.append(stev)

    print(container)
    for stevilo in container:
        for st in container[container.index(stevilo)+1:]:
            if st%stevilo==0:
                container.remove(st)
                continue

    return container

def prastevila(n):
    container = []
    for i in range(2, n):
        if prastevilo(i):
            container.append(i)
    return container

def deljivost(n, d):
    i = 0
    while n%d==0:
        n //= d
        i += 1

    return i

def razcep(n):
    container = []
    pra = prastevila(n)
    for i in pra:
        d = deljivost(n, i)
        if d != 0:
            container.append(d)
    return container

print(razcep(120))


