import seapunknames
import content_array
import random


# grabs a random element from seapunknames.py arrays: 1, 2 and 3 and creates a <title> tag
def generate_title():
    random_title_1 = random.choice(seapunknames.firstArray)
    random_title_2 = random.choice(seapunknames.secondArray)
    random_title_3 = random.choice(seapunknames.thirdArray)
    return "<title>" + random_title_3 + random_title_1 + random_title_2 + random_title_3 + "</title>"


# grabs a random element from seapunknames.py array: 4 and creates a background-image: css property
def generate_background():
    random_background = random.choice(seapunknames.fourthArray)
    return "background-image: url('" + random_background + "')"


# grabs random element from content_array.py array and returns <img> tag
def generate_static_assets():
    random_image = random.choice(content_array.images)
    return "<img src='" + random_image + "' />"


# generate random css properties including: z-index, top, bottom, left right
def generate_css_image_properties():
    random_z_index = random.randint(0,5)
    random_number = random.randint(0,7)
    css_string = "style='z-index: " + str(random_z_index) + ";"
    if random_number > 3:
        left = random.randint(0, 3000)
        css_string = css_string + " left: " + str(left) + "px;"
    if random_number > 4:
        right = random.randint(0,4000)
        css_string = css_string + " right: " + str(right) + "px;"
    if random_number % 2 == 0:
        top = random.randint(0,4000)
        css_string = css_string + " top: " + str(top) + "px;"
    if random_number > 5 == 0:
        bottom = random.randint(0, 3000)
        css_string = css_string + " top: " + str(bottom) + "px;"
    return css_string + "'"



