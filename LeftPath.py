pathChoice = input("Which path will Azmo go down?"
                   ">>> Left        >>> Right")
while pathChoice == "":
    pathChoice = input("Which path will Azmo go down?"
                       "        >>> Left        >>> Right:")
    if pathChoice == "Left" or pathChoice == "Right":
        break
if pathChoice == "Left":
    print("Azmo went down the left path!")
# show cave left
# Slime battle
import sys
from playsound3 import playsound

def hit():
   playsound("hit.mp3")

def battleWon():
    playsound("Win.wav")

def run():
    playsound("run.mp3")

player_hp = 5
slime_hp = 5

    # show Azmo_Fight
    # show Slime_Fight
print("Azmo encounters a slime! What will he do?")
Option1 = "A - Analyse"
Option2 = "B - Slash"
Option3 = "C - Swish tail"
Option4 = "D - Run away"
PlayerChoice1 = "A"
PlayerChoice2 = "B"
PlayerChoice3 = "C"
PlayerChoice4 = "D"
while player_hp > 0 and slime_hp >0:
    print("Your HP: ", player_hp)
    print("Enemy HP: ", slime_hp)
    print(Option1)
    print(Option2)
    print(Option3)
    print(Option4)
    userConclusion = input()
    if userConclusion == PlayerChoice1:
        print("Slime - A common cave enemy, they are easily agitated by others and have a weak skin barrier.")
    elif userConclusion == PlayerChoice2:
        print("Azmo used his claws to slash at the slime! It was badly injured!")
        hit()
        slime_hp = (slime_hp - 2)
    elif userConclusion == PlayerChoice3:
        print("Azmo swished his tail at the slime! This greatly angered it..."
                  "the slimes' attack increased!")
        print("The slime hit Azmo!")
        hit()
        player_hp = (player_hp - 2)
    elif userConclusion == PlayerChoice4:
        print("Azmo ran away!")
        run()
        break
    else:
        print("Wrong input!")
    if slime_hp <= 0:
        print("Azmo defeated the slime!")
        battleWon()
        break
    if player_hp <= 0:
        print("Azmo was badly injured and had to retreat! Battle lost.")
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
        print("Wrong input!")

    if play_again == "yes":
        print("Starting new game...")
        break
    elif play_again == "no":
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("")