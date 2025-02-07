import random
balance = 1000


def supergambler():
    global balance
    print("Your balance: " + str(balance))
    bet = int(input("How much are you betting?: "))
    n1 = int(input("Choose your first number: "))
    n2 = int(input("Choose your second number: "))
    rn1 = random.randint(1, 100)
    print(rn1)
    print("rn1: " + str(rn1))
    rn2 = random.randint(1, 100)
    print("rn2: " + str(rn2))
    if n1 and n2 <= rn1:
        print("Kaching! You won! C1")
        balance = bet*2
        supergambler()
    elif ((n1+n2)%rn2) > rn1:
        print((n1+n2)%rn2)
        print("Kaching! You won! C2")
        balance = bet*2
        supergambler()
    elif n1 or n2 == rn1:
        print("Kaching! You won! C3")
        balance = bet*2
        supergambler()
    else:
        print("You lost. Pay up.")
        balance -= bet
        supergambler()

supergambler()




