def honap():
    szam= int(input("Kérem adjon megy egy hónap sorszámot!"))
    if szam <= 0 or szam >= 13 :
        print("Hiba: a megadott szám nem egy hónap sorszáma")
    else:
        if szam == 1 :
            print("Január")
        elif szam == 2 :
            print("február")
        elif szam == 3 :
            print("március")
        elif szam == 4 :
            print("április")
        elif szam == 5 :
            print("Májús")
        elif szam == 6 :
            print("június")
        elif szam == 7 :
            print("július")
        elif szam == 8 :
            print("Augusztus")
        elif szam == 9 :
            print("Szeptember")
        elif szam == 10 :
            print("Október")
        elif szam == 11 :
            print("November")
        elif szam == 12 :
            print("December")
