def harom ():
    for i in range(0,21):
        print(i)
    for i in range(21):
        print(i)

    for i in range(0,21,1):
        print(i)

    i = 0
    while i<21 :
        print(i)
        i += 1
    pass
def negyes ():
    for i in range(20,57,2):
        print(i)

    while i<58 /2:
        print (i)
    pass


def otos () :
    for i in range(77,-77,-4):
        print(i)

    pass
def beolvas():
    szam = int(input("Kérem adjon meg egy egészszámot"))
    return szam
def hatos ():

    #szam1= float(input("Kérem adj meg egy számot!"))
    #szam2 = float(input("Kérem adj meg mégegy számot!"))

    szam1 = beolvas()
    szam2 = beolvas()

    #melyik a nagyobb
    if szam2< szam1:
        atmenet = szam1
        szam1 = szam2
        szam2 = atmenet
    for i in range(szam1,szam2+1,1):
        print(i, end= " ")
pass

def beolvas():
    szam = int(input("Kérem adjon meg egy egészszámot"))
    return szam
def hetes ():
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1* szam2

    if szorzat< 0:
        for i in range(szorzat-1,1):
            print(i, end= " ")
    else:
        for i in range(0, szorzat+1,1):
            print(i, end=" ")

def nyolcas ():
 def beolvas():
    szam = int(input("Kérem adjon meg egy egészszámot"))
    return szam

    szam1 = beolvas()
    szam2 = beolvas()
    
