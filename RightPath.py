from playsound3 import playsound
import sys

def takeItem():
    playsound("Item.wav")

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
    sys.exit()

elif pathChoice == "Right":
    print("Azmo went down the right path!")
    print("As Azmo ventures further down he happens upon four bushes...")
    bush1 = "Bush 1 - The smallest of the bunch, it only has one lone hanging fruit..."
    bush2 = "Bush 2 - A lush bush full of small purple berries."
    bush3 = "Bush 3 - A large bush littered with spikes! These fruits will be hard to get your hands on."
    bush4 = "Bush 4 - A simple, mundane looking bush, it's fruits look similar to oranges."
    bush_choice1 = "Bush 1"
    bush_choice2 = "Bush 2"
    bush_choice3 = "Bush 3"
    bush_choice4 = "Bush 4"
    print(bush1)
    print(bush2)
    print(bush3)
    print(bush4)
    fruit_decision = ("Yes", "No")
    take_fruit_1 = ("Yes")
    dont_take_fruit = ("No")

while True:
    try:
        fruit_choice = input("Each bush contains a different type of fruit! Which should Azmo investigate?")
        if fruit_choice not in ["Bush 1", "Bush 2", "Bush 3", "Bush 4"]:
            raise ValueError
    except ValueError:
            print("Please type in an acceptable answer. For example: 'Bush 1'")

    if fruit_choice == bush_choice1:
        print("Azmo went to inspect the first bush!")
        print(input("Will Azmo take the fruit from this bush? Yes or No:"))
        if fruit_decision == take_fruit_1:
            print("Azmo took the fruit!")
            takeItem()
        elif fruit_decision == dont_take_fruit:
            print("Azmo didn't take the fruit! Which bush shall he inspect next?")
            print("Azmo took one fruit from the first bush!")
        break
    elif fruit_choice == bush_choice2:
        print("Azmo went to inspect the second bush!")
        print("Will Azmo take the fruit from this bush?")
        fruit_decision = input("")
        break
    elif fruit_choice == bush_choice3:
        print("Azmo went to inspect the third bush!")
        break
    elif fruit_choice == bush_choice4:
        print("Azmo went to inspect the fourth bush!")
        break
    else:
        print("")
