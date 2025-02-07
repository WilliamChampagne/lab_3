import random
balance = 1000

def supergambler():
    global balance
    print("Your balance: " + str(balance))

    ## Choosing your bet and your numbers
    bet = int(input("How much are you betting?: "))
    n1 = int(input("Choose your first number: "))
    n2 = int(input("Choose your second number: "))

    ## Generating random numbers
    rn1 = random.randint(1, 100)
    rn2 = random.randint(1, 100)

    ## Debug print to see the value of rn1 and rn2
    print("rn1: " + str(rn1), "rn2: " + str(rn2))

    ## Gameplay loop
    if n1 >= rn1 and n2 >= rn2:
        print("Kaching! You won! C1")
        balance += bet*2
        supergambler()
    elif ((n1+n2)%rn2) > rn1:
        print((n1+n2)%rn2)
        print("Kaching! You won! C2")
        balance += bet*2
        supergambler()
    elif n1 == rn2 or n2 == rn1:
        print("Kaching! You won! C3")
        balance += bet*2
        supergambler()
    else:
        print("You lost. Pay up.")
        balance -= bet
        supergambler()

supergambler()




