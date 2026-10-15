from playsound3 import playsound

from ChimeraHunt import right_path

def takeItem():
    playsound('Item.wav')

pathChoice = input("Which path will Azmo go down? >>> Left >>> Right")

while pathChoice == "":
    pathChoice = input("Which path will Azmo go down? >>> Left >>> Right:")
    if pathChoice == "Left" or pathChoice == "Right":
        break

if pathChoice == "Left":
    print("Azmo went down the left path!")
elif pathChoice == "Right":
    print("Azmo went down the right path!")
    right_path()

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
            print(f"Azmo took one fruit from {fruit_choice}!")
            has_fruit = True
            fruit_taken = True

        else:
            print("Azmo decided not to take the fruit.")
            print("He should inspect another bush...")

    print("Azmo continues his adventure with his newly acquired fruit!")
    return "fruit"
