print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
def snapikniet():
    return "Sorry, dat snap ik niet.... "

def stapeen():
    bolletjes = int(input("Hoeveel bolletjes wilt u? "))
    if bolletjes >= 1 and bolletjes <= 3:
        return bolletjes
    elif bolletjes >= 4 and bolletjes <= 8:
        return bolletjes
    elif bolletjes >= 9:
        print( "Sorry, zulke grote bakken hebben we niet... " )
        stapeen()
    else:
        print(snapikniet())
        stapeen()

bollen = stapeen()
def staptwee():
    if bollen >= 1 and bollen <= 3:
        hoornbak = input("Wilt u een hoorntje(A) of een bakje(B)?")
        if hoornbak == "A":
            return "U hoorntje met ", bollen, " bolletjes!"
        elif hoornbak == "B":
            return "Uw bakje met ", bollen, " bolletjes!!"
        else:
            print(snapikniet())
            staptwee()
    elif bollen >= 4 and bollen <= 8:
        return "Dan krijgt u van mij een bakje met ", bollen, " bolletjes"

twee = staptwee()
def stapdrie():
    if twee == int(twee):
        print(twee)
        einde = input(twee ,"Wilt u nog meer bestellen? (Y/N)")
        if einde == "Y":
            stapeen()
        elif einde == "N":
            print("Bedankt en tot ziens! ")
        else:
            print(snapikniet(), stapdrie())

print(stapeen())