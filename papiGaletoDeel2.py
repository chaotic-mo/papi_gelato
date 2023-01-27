from calendar import month_abbr
box =[]
def sorry():
    print('Sorry dat begrijp ik niet ')
 
def stap1():
    global hoeveel
    try:
        hoeveel = int(input('hoeveel bolletjes wilt u? '))
        if hoeveel >= 1 and hoeveel <= 3:
            stap2()
        elif hoeveel >= 4 and hoeveel <= 8  :
            stap3()
        elif hoeveel > 8: 
            print('sorry zulke grote bakken hebben we niet!')
            stap1()
    except ValueError:
        sorry()
        return stap1()
    
def stap2():
    global HornOfBak
    HornOfBak = input(f'wilt u deze {hoeveel} bollen in een A)Horrentje of B) Bakje ')
    HornOfBak = HornOfBak.lower()
    if HornOfBak == 'a':
        HornOfBak = 'Horrentje'
        stap3()
    elif HornOfBak == 'b':
        HornOfBak = 'Bakje'
        stap3()
    else:
        sorry()
        stap2()
        
def stap3():
    global HornOfBak, hoeveel
    if hoeveel >= 4 and hoeveel <= 8:
        print(f'hier is uw Bakje met {hoeveel} bollen')
        box.append(f'hier is uw Bakje met {hoeveel} bollen')
    else:
        print(f'hier is uw {HornOfBak} met {hoeveel} bollen')
        box.append(f'hier is uw {HornOfBak} met {hoeveel} bollen')
    def stap3v2():
        herhalen = input('wilt u nog meer bestellen?(Y/N)')
        herhalen = herhalen.lower()
        if herhalen == 'y':
            stap1()
        elif herhalen == 'n':
            for i in box:
                print(i)
            print('bedankt en tot ziens!')
            
        else:
            sorry()
            stap3v2()
    stap3v2()
    
stap1()
