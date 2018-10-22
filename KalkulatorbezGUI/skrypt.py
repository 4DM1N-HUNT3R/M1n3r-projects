def Zatwierdz():
    a = int(raw_input("Podaj pierwsza liczbe: "))
    b = int(raw_input("Podaj druga liczbe: "))
    if a > 0 and b > 0: 
        while a > 0 and b > 0: 
            if a > b : 
                a = a % b
            else: 
                b = b % a 
            if a > b: 
                print ("NWD = ", a) 
            else: 
                print ("NWD = ", b)
    else: 
        print "Podaj zmienna a i b wieksza od zera" 
