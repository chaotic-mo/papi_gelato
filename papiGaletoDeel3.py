print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is. ")
box = []

def sorry():
    print("Sorry, dat snap ik niet... ")

def stapeen():
    global bolletjes
    #first front order
    try:
        bolletjes = int(input("Hoeveel bolletjes wilt u? "))
        if bolletjes >= 1 and bolletjes <= 3:
            staptwee()
        elif bolletjes >= 4 and bolletjes <=8:
            staplaatste()
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
        staplaatste()
    elif HornOfBak == 'b':
        HornOfBak = 'Bakje'
        staplaatste()
    else:
        sorry()
        staptwee()

def staplaatste():
    #third end order
    global HornOfBak, bolletjes
    if bolletjes >= 4 and bolletjes <= 8:
        print(f'Hier is uw Bakje met {bolletjes} bollen. ')
        box.append(f'Hier is uw Bakje met {bolletjes} bollen. ')
    else:
        print(f'Hier is uw {HornOfBak} met {bolletjes} bollen. ')
        box.append(f'Hier is uw {HornOfBak} met {bolletjes} bollen. ')
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