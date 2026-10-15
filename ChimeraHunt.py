import sys

# Tracks whether the player has collected a fruit
has_fruit = False

# This makes sound effects optional. The game will still work without them
try:
    from playsound3 import playsound
except ImportError:
    playsound = None


def play_sound(filename):
    try:
        if playsound is not None:
            playsound(filename)
    except Exception:
        pass


def hit():
    play_sound("hit.mp3")


def battleWon():
    play_sound("Win.wav")


def run():
    play_sound("run.mp3")


def battleLost():
    play_sound("gameoversound.mp3")


def takeItem():
    play_sound("Item.wav")


def gameOverScreen():
    print("""                                                                                   
         ▄▄▄▄▄▄▄    ▄▄▄▄   ▄▄▄      ▄▄▄  ▄▄▄▄▄▄▄     ▄▄▄▄▄   ▄▄▄▄  ▄▄▄▄  ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄   
        ███▀▀▀▀▀  ▄██▀▀██▄ ████▄  ▄████ ███▀▀▀▀▀   ▄███████▄ ▀███  ███▀ ███▀▀▀▀▀ ███▀▀███▄ 
        ███       ███  ███ ███▀████▀███ ███▄▄      ███   ███  ███  ███  ███▄▄    ███▄▄███▀ 
        ███  ███▀ ███▀▀███ ███  ▀▀  ███ ███        ███▄▄▄███  ███▄▄███  ███      ███▀▀██▄  
        ▀██████▀  ███  ███ ███      ███ ▀███████    ▀█████▀    ▀████▀   ▀███████ ███  ▀███ 
                                                                                           """)

    while True:
        play_again = input("Would you like to play again ? [yes/no]: ").strip().lower()
        if play_again == "yes":
            print("Starting new game...")
            return "restart"
        elif play_again == "no":
            print("Thanks for playing! Goodbye!")
            sys.exit()
        else:
            print("Please enter either 'yes' or 'no'")


# Title Screen
def show_title():
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


# Tutorial
def tutorial():
    print("===========================================================================================================")
    print("Welcome to the tutorial.")
    print("You are playing as Azmo in Chimera Hunt.")
    print("You will explore a cave and choose between two paths.")
    print("Type the options shown on the screen to make your choices.")
    print("During battle you'll have four choices to pick from, use context clues to figure out which to choose!")
    print("Your HP represents your health. If it reaches zero, you lose the battle and reach a game over.")
    print("Enjoy your adventure!")
    print(" ")
    print("===========================================================================================================")
    print(" ")


# Slime Battle
def slime_battle():
    player_hp = 5
    slime_hp = 5

    print("Azmo encounters a slime! What will he do?")
    print("=========================================")

    Option1 = "A - Analyse"
    Option2 = "B - Slash"
    Option3 = "C - Swish tail"
    Option4 = "D - Run away"

    while player_hp > 0 and slime_hp > 0:
        print("Your HP: ", player_hp)
        print("Enemy HP: ", slime_hp)
        print(Option1)
        print(Option2)
        print(Option3)
        print(Option4)
        print("=========================================")

        userConclusion = input().strip().upper()

        if userConclusion == "A":
            print("Slime - A common cave enemy, easily agitated and has a weak skin barrier.")

        elif userConclusion == "B":
            print("Azmo used his claws to slash at the slime! It was badly injured!")
            hit()
            slime_hp -= 2

        elif userConclusion == "C":
            print("Azmo swished his tail at the slime! This greatly angered it...")
            print("The slime hit Azmo!")
            hit()
            player_hp -= 2

        elif userConclusion == "D":
            print("Azmo ran away!")
            run()
            return "ran"

        else:
            print("Wrong input!")
            continue

        if player_hp <= 0:
            print("Azmo was badly injured and had to retreat!")
            battleLost()
            return gameOverScreen()

        if slime_hp <= 0:
            print("Azmo defeated the slime!")
            battleWon()
            print("Azmo continues to go further through the cave after defeating the slime!")
            return "won"


# Right path
def right_path():
    global has_fruit

    print("As Azmo ventures further down he happens upon four bushes...")

    bush_descriptions = {
        "BUSH 1": """Bush 1 - The smallest of the bunch, it only has one lone hanging fruit...
       (   )
      (     )
       |   |
      (  o  )
       |   | """,

        "BUSH 2": """Bush 2 - A lush bush full of small purple berries.
       (~~~~~~)
      ( ~ oo ~ )
     ( ~ oooo ~ )
      ( ~ oo ~ )
       (~~~~~~) """,

        "BUSH 3": """Bush 3 - A large bush littered with spikes!
       /\\/\\/\\/\\
      /\\/\\^^/\\/\\
     /\\/\\^^^^/\\/\\
      \\/\\^^^^/\\/
       \\/\\/\\/\\/ """,

        "BUSH 4": """Bush 4 - A simple, mundane looking bush, its fruits look similar to oranges.
        (     )
       (  o o  )
      (   o    )
       (     )
        (___) """
    }

    fruit_taken = False

    while not fruit_taken:

        fruit_choice = input(
            "Which bush should Azmo investigate? (Bush 1 / Bush 2 / Bush 3 / Bush 4): ").strip().upper()

        if fruit_choice not in bush_descriptions:
            print("Please type in an acceptable answer. For example: 'Bush 1'")
            continue

        print(bush_descriptions[fruit_choice])

        fruit_decision = input("Will Azmo take the fruit from this bush? (Yes/No): ").strip().lower()

        while fruit_decision not in ["yes", "no"]:
            print("Please enter Yes or No.")
            fruit_decision = input("Will Azmo take the fruit from this bush? (Yes/No): ").strip().lower()

        if fruit_decision == "yes":
            takeItem()
            print("Azmo took one fruit from {fruit_choice}!")
            has_fruit = True
            fruit_taken = True

        else:
            print("Azmo decided not to take the fruit.")
            print("He should inspect another bush...")

    print("Azmo continues his adventure with his newly acquired fruit!")
    return "fruit"


# Final Battle — Megabat
def megabat_battle():
    global has_fruit

    player_hp = 5
    megabat_hp = 5

    print("Azmo encounters a Megabat! What will he do?")
    print("=========================================")
    Decision1 = "A - Analyse"
    Decision2 = "B - Flap wings"
    Decision3 = "C - Bribe with fruit"
    Decision4 = "D - Run away"

    while player_hp > 0 and megabat_hp > 0:
        print("Your HP:", player_hp)
        print("Enemy HP:", megabat_hp)
        print(Decision1)
        print(Decision2)
        print(Decision3)
        print(Decision4)
        print("=========================================")

        Option = input().strip().upper()

        if Option == "A":
            print("Megabat - A huge bat well-known for its large wings, capable of creating huge gusts of wind.")

        elif Option == "B":
            print("Azmo flapped his wings...but the Megabat flapped back!")
            print("Its strong gusts of wind made Azmo faint!")
            hit()
            player_hp -= 5

        elif Option == "C":
            if not has_fruit:
                print("Azmo thought about bribing the Megabat with some fruit...")
                print("...but he didn't have any! Perhaps he should go back and find some...")
                return "no_fruit"
            else:
                print("Azmo bribed the Megabat with some fruit! The Megabat got occupied eating!")
                print("Azmo quietly slips past it and finds the hidden treasure!")
                battleWon()
                print("✨ YOU WIN! Azmo has conquered the cave and claimed the treasure! ✨")
                return "won"

        elif Option == "D":
            print("Azmo ran away!")
            print("Returning to the start of the game...")
            run()
            return "back_to_fork"

        else:
            print("Wrong input!")
            continue

        if player_hp <= 0:
            print("Azmo was severely injured! Battle lost.")
            battleLost()
            return gameOverScreen()


# Main Game
def start_game():
    global has_fruit
    has_fruit = False  # Resets fruit status each new game

    show_title()

    while True:
        print("Welcome to Chimera Hunt! Would you like a tutorial?")
        choice1 = input("Press 1 for tutorial, 2 to continue, or 3 to exit: ").strip()

        if choice1 == "1":
            tutorial()
            break
        elif choice1 == "2":
            break
        elif choice1 == "3":
            print("Thanks for playing Chimera Hunt!")
            sys.exit()
        else:
            print("Incorrect input. Please enter 1, 2, or 3.")

    print(
        "Azmo walks towards the entrance of the cave...he's here on a quest to find a hidden treasure within this cave...")
    print("He happens across two separate paths.")
    print("The left path has small pieces of gold trailing along the cave floor.")
    print("The right path has a few interesting looking fruits across the floor.")
    print("""
                     ___
                  .-'   `-.
                 /  LEFT   \\
            *   /           \\   *
    ---------  /             \\  ---------
             .'               `.
            /   RIGHT          \\
           /                     \\
          '-----------------------'
    """)

    while True:
        pathChoice = input("Which path will Azmo go down? >>> Left >>> Right: ").strip().upper()

        if pathChoice == "LEFT":
            print("Azmo went down the left path!")
            result = slime_battle()

            if result == "ran":
                while True:
                    play_again = input("Would you like to play again? [yes/no]: ").strip().lower()
                    if play_again == "yes":
                        print("Starting new game...")
                        return "restart"
                    elif play_again == "no":
                        print("Thanks for playing! Goodbye!")
                        sys.exit()
                    else:
                        print("Please enter 'yes' or 'no'.")
                break

            if result == "restart":
                return "restart"

            break

        elif pathChoice == "RIGHT":
            print("Azmo went down the right path!")
            right_path()
            break

        else:
            print("Incorrect input. Please type Left or Right.")

    print("Azmo proceeds deeper into the cave...and there before him is the treasure!")
    print("But a shadow looms overhead...")

    return megabat_battle()


# Game Loop
def main():
    while True:
        result = start_game()

        if result == "restart":
            continue

        if result == "back_to_fork":
            continue

        if result == "no_fruit":
            continue

        while True:
            play_again = input("Would you like to play again? [yes/no]: ").strip().lower()

            if play_again == "yes":
                print("Starting new game...")
                break
            elif play_again == "no":
                print("Thanks for playing! Goodbye!")
                return
            else:
                print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()