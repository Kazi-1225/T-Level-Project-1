# Final Battle
import sys
from playsound3 import playsound

def hit():
    playsound("hit.mp3")

def run():
    playsound("run.mp3")

player_hp = 5
Megabat_hp = 5

    # show Azmo_Fight
    # show Megabat_Fight
print("Azmo encounters a Megabat! What will he do?")
Decision1 = "A - Analyse"
Decision2 = "B - Flap wings"
Decision3 = "C - Bribe with fruit"
Decision4 = "D - Run away"
PlayerInput1 = "A"
PlayerInput2 = "B"
PlayerInput3 = "C"
PlayerInput4 = "D"
while player_hp > 0 and Megabat_hp > 0:
    print ("Your HP: ", player_hp)
    print ("Enemy HP: ", Megabat_hp)
    print (Decision1)
    print (Decision2)
    print (Decision3)
    print (Decision4)
    Option = input()
    if Option == PlayerInput1:
        print("Megabat - A huge bat well-known for its large wings, capable of creating huge gusts of wind, they travel through caves in search of food.")
    elif Option == PlayerInput2:
        print("Azmo flapped his wings...but the Megabat flapped back!"
            "It's strong gusts of wind made Azmo faint!")
        player_hp = (player_hp - 5)
        hit()
    # show battle lost screen
    elif Option == PlayerInput3:
        print("Azmo bribed the Megabat with some fruit! The Megabat got occupied eating!")
        break
    elif Option == PlayerInput4:
        print("Azmo ran away!")
        run()
        break
    else:
        print("Wrong input!")
    # show cave bg
    if player_hp <= 0:
        print("Azmo was severely injured! "
              "Battle lost.")
        print("""                                                                                   
                 ▄▄▄▄▄▄▄    ▄▄▄▄   ▄▄▄      ▄▄▄  ▄▄▄▄▄▄▄     ▄▄▄▄▄   ▄▄▄▄  ▄▄▄▄  ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄   
                ███▀▀▀▀▀  ▄██▀▀██▄ ████▄  ▄████ ███▀▀▀▀▀   ▄███████▄ ▀███  ███▀ ███▀▀▀▀▀ ███▀▀███▄ 
                ███       ███  ███ ███▀████▀███ ███▄▄      ███   ███  ███  ███  ███▄▄    ███▄▄███▀ 
                ███  ███▀ ███▀▀███ ███  ▀▀  ███ ███        ███▄▄▄███  ███▄▄███  ███      ███▀▀██▄  
                ▀██████▀  ███  ███ ███      ███ ▀███████    ▀█████▀    ▀████▀   ▀███████ ███  ▀███ 

                                                                                                   """)

        while True:
            try:
                play_again = input("Would you like to play again ? [yes/no]: ")
                if play_again not in ["yes", "no"]:
                    raise ValueError
            except ValueError:
                print("Please enter 'yes' or 'no'")

            if play_again == "yes":
                print("Starting new game...")
                break
            elif play_again == "no":
                print("Thanks for playing! Goodbye!")
                sys.exit()
            else:
                print("")