# Start Menu
import sys

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


print("Welcome to Chimera Hunt! Would you like a tutorial?")
choice1 = input("Press 1 to view the tutorial, press 2 to continue without it. Press 3 to exit the game."
                " ")
if choice1 == 3:
    sys.exit()

elif choice1 == 1:
    print("Welcome to the tutorial.")

else:
    # show Cave Enter
    print("Azmo walks towards the entrance of the cave, slowly entering, unbeknownst to what awaits him inside...")
    print("Azmo happens across two separate paths.")
    print("The right path has small pieces of gold trailing along the cave floor, further into it.")
    print("The left path has a few interesting looking fruits scattered across the floor.")
pathChoice = input("Which path will Azmo go down?"
                   ">>> Left        >>> Right")
while pathChoice == "":
    pathChoice = input("Which path will Azmo go down?"
                       "        >>> Left        >>> Right:")
    if pathChoice == "Left" or pathChoice == "Right":
        break
if pathChoice == "Left":
    print("Azmo went down the left path!")
    #SlimeBattle()
    # show Cave_Left
elif pathChoice == "Right":
    print("Azmo went down the right path!")
    # show Cave_Right
else:
    print("Incorrect input. Try again.")
