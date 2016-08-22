import seapunknames
import random


# function that grabs a random element from seapunknames.py arrays: 1, 2 and 3 and creates a <title> tag
def generate_title():
    random_title_1 = random.choice(seapunknames.firstArray)
    random_title_2 = random.choice(seapunknames.secondArray)
    random_title_3 = random.choice(seapunknames.thirdArray)
    return "<title>" + random_title_3 + random_title_1 + random_title_2 + random_title_3 + "</title>"


# function that grabs a random element from seapunknames.py array: 4 and creates a background-image: css property
def generate_background():
    random_background = random.choice(seapunknames.fourthArray)
    return "background-image: url('" + random_background + "')"

