#függvény
def egeszBeolvas() :
    szam =float(input("Kérem adjon meg egy számot!"))
    return szam
#eljárás
def teglalap () :

    oldal1 = egeszBeolvas()
    oldal2 = egeszBeolvas()

    if (oldal1 > 0 and oldal2 > 0) :
        kerulet = round(2* oldal1 + oldal2, 2)
        terulet = round(oldal1 * oldal2, 2)
        print("a téglalap területe:"+str(terulet)+",kerülete:"+str(kerulet)+'.')
    else:
        print("Hiba:a téglalap oldalai nem pozitívak!")
