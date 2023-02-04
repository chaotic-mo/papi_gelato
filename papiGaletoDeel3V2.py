print("Welkom bij Papi Gelato we hebben nu nieuwe smaken zoals: Aarbei!, Chocolade! maar ook de OG! Vanille!!. ")
box = []

LITERS = 9.80

BOLLETJES = 0.95
HORENTJE = 1.25
BAKJES = 0.75

SLAGROOM = 0.50
SPRINKELS = 0.30
CARAMELSAUSA = 0.60
CARAMELSAUSB = 0.90
toppingstotaal = 0

totaalbolletjes = 0
totaalhorentjes = 0
totaalbakjes = 0
totaal = 0

def sorry():
    print("Sorry, dat is geen optie die we aanbieden... ")

def stapnul():
    global bizunizu
    bizunizu = int(input("Bent u 1) particulier of 2) zakelijk? "))
    if bizunizu == 1:
        stapeen()
    elif bizunizu == 2:
        stapeenzakelijk()
    else:
        sorry()
        stapnul()

def stapeenzakelijk():
    global aantalliters
    aantalliters = int(input("Hoeveel liter ijs wilt u? "))
    stapdrie()
    

def stapeen():
    global bolletjes, HornOfBak
    #first front order
    try:
        bolletjes = int(input("Hoeveel bolletjes wilt u? "))
        if bolletjes >= 1 and bolletjes <= 3:
            staptwee()
        elif bolletjes >= 4 and bolletjes <=8:
            HornOfBak = 'Bakje'
            stapdrie()
        elif bolletjes > 8:
            print("Sorry, zulke grote bakken hebben we niet... ")
            stapeen()
    except ValueError:
        sorry()
        return stapeen()

def staptwee():
    #second middle order
    global HornOfBak
    HornOfBak = input(f'Wilt u deze {bolletjes} bollen in een A) Horrentje of B) Bakje? ')
    HornOfBak = HornOfBak.lower()
    if HornOfBak == 'a':
        HornOfBak = 'Horrentje'
        stapdrie()
    elif HornOfBak == 'b':
        HornOfBak = 'Bakje'
        stapdrie()
    else:
        sorry()
        staptwee()

def stapdrie():
    global bolletjes, smaken, bizunizu
    smaken = []
    aantalsmaken = 0
    if bizunizu == 1:
        aantalsmaken = bolletjes
    else:
        aantalsmaken = aantalliters
    for i in range(aantalsmaken):
        smaak = input(f"Welke smaak wilt u " + str(i+1) + "? A) Aardbei, C) Chocolade of V) Vanille? ")
        smaak = smaak.lower()
        if smaak == 'a':
            smaken.append('aardbei')
        elif smaak == 'c':
            smaken.append('chocolade')
        elif smaak == 'v':
            smaken.append('vanille')
        else:
            sorry()
            stapdrie()
    if bizunizu == 1:
        toppings()
    else:
        stapbon()

def toppings():
    global toppingstotaal, bolletjes, smaken, HornOfBak
    top = input("Wilt u een topping? A) geen, B) slagroom, C) sprinkels of D) Carmelsaus? ")
    top = top.lower()
    if top == 'a':
        staplaatste()
    elif top == 'b':
        toppingstotaal += SLAGROOM
    elif top == 'c':
        toppingstotaal += SPRINKELS  * bolletjes	
    elif top == 'd':
        if HornOfBak == 'Horrentje':
            toppingstotaal += CARAMELSAUSA
        else:
            toppingstotaal += CARAMELSAUSB
    else:
        sorry()
        toppings()
    staplaatste()

def stapbon():
    global totaal, totaalbakjes, totaalbolletjes, totaalhorentjes, toppingstotaal
    print('''----["Papi gelato"]----\n''')
    if bizunizu == 1:
        print(f"uw totalebollen is: {totaalbolletjes} x € {format(BOLLETJES, '.2f')} = € {format(totaalbolletjes * BOLLETJES, '.2f')}")
        if totaalhorentjes > 0: 
            print(f"uw totalehorrentje is: {totaalhorentjes} x € {format(HORENTJE, '.2f')} = € {format(totaalhorentjes * HORENTJE, '.2f')}")
        if totaalbakjes > 0: 
            print(f"uw totalebakken is: {totaalbakjes} x € {format(BAKJES, '.2f')} = € {format(totaalbakjes * BAKJES, '.2f')}")
        if toppingstotaal > 0:
            print(f"uw toppings koste is: 1 x € {format(toppingstotaal, '.2f')} = € {format(toppingstotaal, '.2f')}")

        totaalprijs = (totaalbolletjes * BOLLETJES) + (totaalhorentjes * HORENTJE) + (totaalbakjes * BAKJES) + (toppingstotaal)
        
        print("--------------------------- + \n",f"uw totaal prijs = € {format(totaalprijs, '.2f')}")
    else:
        print(f"Liter {aantalliters} x € {format(LITERS, '.2f')} = € {format(aantalliters * LITERS, '.2f')}" )
        print(f"--------------------------- + \nTotaal = € {format(aantalliters * LITERS, '.2f')} \n BTW (9%)  € {format(aantalliters * LITERS / 100 * 9, '.2f')}")
            
def staplaatste():
    #third end order
    global HornOfBak, bolletjes, smaken, totaal, totaalbakjes, totaalbolletjes, totaalhorentjes, toppingstotaal

    smaken_str = ', '.join(smaken)
    bericht = f'Hier is uw {HornOfBak} met {bolletjes} bollen en de smaken {smaken_str}. '
    print(bericht)
    box.append(bericht)

    totaalbolletjes += bolletjes

    if HornOfBak == 'Horrentje':
        totaalhorentjes += 1
    elif HornOfBak == 'Bakje':
        totaalbakjes += 1

    staplaatstev2()

def staplaatstev2():
    herhalen = input('wilt u nog meer bestellen?(Y/N) ')
    herhalen = herhalen.lower()
    if herhalen == 'y':
        for i in box:
            print(i)
        stapeen()
    elif herhalen == 'n':
        stapbon() 
    else:
        sorry()
        staplaatstev2()

stapnul()