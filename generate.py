import seapunknames
import random


def generate_title():
    rand1 = random.choice(seapunknames.firstArray)
    rand2 = random.choice(seapunknames.secondArray)
    rand3 = random.choice(seapunknames.thirdArray)
    # rand4 = random.choice(seapunknames.fourthArray)
    return "<title>" + rand3 + rand1 + rand2 + rand3 + "</title>"



