# Final Battle
from playsound3 import playsound

def hit():
    playsound("hit.mp3")

def battle (player_hp: int , enemy_hp: int):
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
    while player_hp > 0 and enemy_hp > 0:
        print ("Your HP: ", player_hp)
        print ("Enemy HP: ", enemy_hp)
        print (Decision1)
        print (Decision2)
        print (Decision3)
        print (Decision4)
        Option = input()
        if Option == PlayerInput1:
            print("Megabat - A huge bat well-known for its large wings, capable of creating huge gusts of wind, they travel through caves in search of food.")
        if Option == PlayerInput2:
            print("Azmo flapped his wings...but the Megabat flapped back!"
            "It's strong gusts of wind made Azmo faint!")
            hit()
    # show battle lost screen
        if Option == PlayerInput3:
            print("Azmo bribed the Megabat with some fruit! The Megabat got occupied eating!")
        elif Option == PlayerInput4:
            print("Azmo ran away!")
    # show cave bg

battle(5, 5)