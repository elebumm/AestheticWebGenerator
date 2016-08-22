import seapunknames
import content_array
import font_matrix
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
    if random_number > 1 and random_number < 5:
        left = random.randint(0, 3000)
        css_string = css_string + " left: " + str(left) + "px;"
    if random_number >= 3:
        right = random.randint(0,4000)
        css_string = css_string + " right: " + str(right) + "px;"
    if random_number <= 2:
        top = random.randint(0,4000)
        css_string = css_string + " top: " + str(top) + "px;"
    if random_number % 2 == 0:
        bottom = random.randint(0, 3000)
        css_string = css_string + " bottom: " + str(bottom) + "px;"
    return css_string + "'"


# generate complete image tag for static asset by concatenating results from generate_static_assets()
# and generate_css_image_properties()
def generate_complete_image_tag(static_asset, css_string):
    html_string = static_asset
    css = css_string

    # insert generated css into image tag
    html_string = html_string[:5] + css + html_string[4:]
    return html_string


# generate css values for web page, takes background_image argument passed by generate_background()
# and assigns random font from font_matrix
def generate_css_body_properties(background_image):
    background = background_image
    font_family = "Times New Roman, sans-serif"
    random_number = random.randint(0,2)
    css_string = "body: {\n"
    font_face_css = "\n@font-face { \nfont-family: '"

    css_string = css_string + background + ";"

    if random_number == 2:
        css_string = css_string + "\nfont-family: " + font_family + ";"
    elif random_number == 0:
        font_family = font_matrix.fonts[0][0]
        font_source = font_matrix.fonts[0][1]
        font_face_css = font_face_css + font_family + "'; src: url('" + font_source + "');"
        css_string = css_string + font_face_css
    else:
        font_family = str(font_matrix.fonts[random_number][0])
        font_source = str(font_matrix.fonts[random_number][1])
        font_face_css = font_face_css + font_family + "'; src: url('" + font_source + "');"
        css_string = css_string + font_face_css
    return css_string + "\n}"
