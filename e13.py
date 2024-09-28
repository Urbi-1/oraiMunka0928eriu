import math
def tizenharim () :

    #

    r = float(input("Kérem adjon meg egy kör sugár értéket!"))
    if (r > 0) :
        terulet = r**2 * math.pi
        terulet = r*r *math.pi
        terulet = math.pow(r, 2)* math.pi
        terulet = pow(r, 2) * math.pi
        kerulet = math.pi * 2 * r

        print(" A kör területe:"+ str(terulet)+ "a kör kerülete:"+ str(kerulet) + '.')
    else:
        print("Hiba: A kör sugara nem pozitív!")


