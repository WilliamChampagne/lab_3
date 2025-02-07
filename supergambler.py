import random

## Argent du joueur. Si cette valeur tombe à 0, le joueur perd et recommence le jeu.
balance = 1000
## Round du jeu. Augmente la difficulté du jeu.
round = 1

def supergambler():
    global balance, round

    print("Round: " + str(round))

    ## Loss condition check
    if balance <= 0:
        print("You are out of money. You lost. Starting new game...\n")
        balance = 1000
        round =  1
        supergambler()
    else:
        pass

    print("Your balance: " + str(balance))

    ## Choosing your bet and checking if you have enough
    ## Bet est la mise que le jouer débourse pour participer au jeu. Si le joueur perde le jeu, il perd l'entièreter de sa mise.
    bet = int(input("\nHow much are you betting?: "))
    if bet > balance:
        print("You do not have enough money for that bet.\n")
        supergambler()
    else:
        pass

    ## Choosing your numbers 
    n1 = int(input("\nChoose your first number: "))
    while n1 < 1 or n1 > 100:
        n1 = int(input("Numbers must be between 1 and 100. Please select your new number: "))

    n2 = int(input("Choose your second number: "))
    while n2 < 1 or n2 > 100:
        n2 = int(input("Numbers must be between 1 and 100. Please select your new number: "))

    ## Generating random numbers
    rn1 = random.randint(1, 100)
    rn2 = random.randint(1, 100)

    ## Debug print to see the value of rn1 and rn2 (remove double comment markers to print debug)
    ## print("rn1: " + str(rn1), "rn2: " + str(rn2))

    ## - Gameplay loop -
    ## Il y a 3 conditions pour gagner le jeu. Les conditions sont basés sur les numéros choisie par l'utilisateur et les numéros randoms.
    ## Les numéros choisie par l'utilisateur seront comparé au nombres généré par le code, un peut comme la roue de la chance. 
    ## Les conditions de victoires sont déterminées par des calculs mathématiques utilisant tout les numéros choisie par le joueur et le code.
    if n1 >= rn1 and n2 >= rn2:
        print("\nKaching! You won!")
        balance += bet*2
        print("You have won: " + str(bet*2) + "$")
        round += 1
        supergambler()
    elif ((n1+n2)%rn2) > rn1:
        print((n1+n2)%rn2)
        print("\nKaching! You won!")
        balance += bet*2
        print("You have won: " + str(bet*2) + "$")
        round += 1
        supergambler()
    elif n1 == rn2 or n2 == rn1:
        print("\nKaching! You won!")
        balance += bet*2
        print("You have won: " + str(bet*2) + "$")
        round += 1
        supergambler()
    else:
        print("\nYou lost. Pay up.")
        balance -= bet+(bet*((round/10))-10)
        print("You have lost: " + str(bet+(bet*((round/10))-10)) + "$")
        supergambler()

supergambler()




