print("Welkom bij Papi Gelato we hebben nieuwe smaken zoals: Aarbei!, Chocolade!, Munt! maar ook de og Vanille!!. ")
box = []

def sorry():
    print("Sorry, dat snap ik niet... ")

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
    HornOfBak = input(f'Wilt u deze {bolletjes} bollen in een A)Horrentje of B) Bakje ')
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
    global bolletjes, smaken
    smaken = []
    for i in range(bolletjes):
        smaak = input(f"Welke smaak wilt u voor bolletje nummer "+str(i+1)+"? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
        smaak = smaak.lower()
        if smaak == 'a':
            smaken.append('aardbei')
        elif smaak == 'c':
            smaken.append('chocolade')
        elif smaak == 'm':
            smaken.append('munt')
        elif smaak == 'v':
            smaken.append('vanille')
        else:
            sorry()
            stapdrie()
    staplaatste()


def staplaatste():
    #third end order
    global HornOfBak, bolletjes, smaken

    smaken_str = ', '.join(smaken)
    bericht = f'Hier is uw {HornOfBak} met {bolletjes} bollen en de smaken {smaken_str}. '
    print(bericht)
    box.append(bericht)

    staplaatstev2()

def staplaatstev2():
    herhalen = input('wilt u nog meer bestellen?(Y/N) ')
    herhalen = herhalen.lower()
    if herhalen == 'y':
        stapeen()
    elif herhalen == 'n':
        for i in box:
            print(i)
        print('bedankt en tot ziens! ')  
    else:
        sorry()
        staplaatstev2()

stapeen()