# Start Menu
# Slime battle
import sys
from playsound3 import playsound

def gameOverScreen():
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
                sys.exit()
            else:
                print("")

def hit():
   playsound("hit.mp3")

def battleWon():
    playsound("Win.wav")

def run():
    playsound("run.mp3")

def battleLost():
    playsound("gameoversound.mp3")

def slimebattle():
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
            battleLost()
            gameOverScreen()

# Title Screen

print("""
  /$$$$$$  /$$       /$$                                                  /$$   /$$                       /$$    /$$
 /$$__  $$| $$      |__/                                                 | $$  | $$                      | $$   | $$
| $$  \\__/| $$$$$$$  /$$ /$$$$$$/$$$$   /$$$$$$   /$$$$$$  /$$$$$$       | $$  | $$ /$$   /$$ /$$$$$$$  /$$$$$$ | $$
| $$      | $$__  $$| $$| $$_  $$_  $$ /$$__  $$ /$$__  $$|____  $$      | $$$$$$$$| $$  | $$| $$__  $$|_  $$_/ | $$
| $$      | $$  \\ $$| $$| $$ \\ $$ \\ $$| $$$$$$$$| $$  \\__/ /$$$$$$$      | $$__  $$| $$  | $$| $$  \\ $$  | $$   |__/
| $$    $$| $$  | $$| $$| $$ | $$ | $$| $$_____/| $$      /$$__  $$      | $$  | $$| $$  | $$| $$  | $$  | $$ /$$
|  $$$$$$/| $$  | $$| $$| $$ | $$ | $$|  $$$$$$$| $$     |  $$$$$$$      | $$  | $$|  $$$$$$/| $$  | $$  |  $$$$//$$
 \\______/ |__/  |__/|__/|__/ |__/ |__/ \\_______/|__/      \\_______/      |__/  |__/ \\______/ |__/  |__/   \\___/ |__/

 """)


print("Welcome to Chimera Hunt!")
choice1 = input("Press 1 to view the tutorial, press 2 to continue without it. Press 3 to exit the game."
                " ")
if choice1 == "3":
    print("Exiting game...")
    sys.exit()

elif choice1 == "1":
    print("Welcome to the tutorial.")

else:
    # show Cave Enter
    print("Azmo walks towards the entrance of the cave, slowly entering, unbeknownst to what awaits him inside...")
    print("Azmo happens across two separate paths.")
    print("The right path has small pieces of gold trailing along the cave floor, further into it.")
    print("The left path has a few interesting looking fruits scattered across the floor.")
while True:
    try:
        pathChoice = input("Which path will Azmo go down?"
                            ">>> Left        >>> Right")
        if pathChoice not in ["Left", "Right"]:
            raise ValueError
    except ValueError:
        print("Please type either 'Left' or 'Right'.")
    if pathChoice == "Left" or pathChoice == "Right":
        break
if pathChoice == "Left":
    print("Azmo went down the left path!")
    slimebattle()
    # show Cave_Left
elif pathChoice == "Right":
    print("Azmo went down the right path!")
    # show Cave_Right
