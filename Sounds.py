from playsound3 import playsound

def takeItem():
    playsound("Item.wav")

def hit():
    playsound("hit.mp3")

def battleWon():
    playsound("Win.wav")

def battleLost():
    playsound("gameoversound.mp3")

takeItem()
hit()
battleWon()
battleLost()
