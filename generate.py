import seapunknames
import content_array
import font_matrix
import random
from faker import Faker

fake = Faker()


# grabs a random element from seapunknames.py arrays: 1, 2 and 3 and creates a <title> tag
def gen_title():
    random_title_1 = random.choice(seapunknames.firstArray)
    random_title_2 = random.choice(seapunknames.secondArray)
    random_title_3 = random.choice(seapunknames.thirdArray)
    return "<title>" + random_title_3 + random_title_1 + random_title_2 + random_title_3 + "</title>"


# grabs a random element from seapunknames.py array: 4 and creates a background-image: css property
def gen_background():
    random_background = random.choice(seapunknames.fourthArray)
    return "background-image: url('" + random_background + "')"


# grabs random element from content_array.py array and returns <img> tag
def gen_static_assets():
    random_image = random.choice(content_array.images)
    return "<img src='" + random_image + "' />"


# generate random css properties including: z-index, top, bottom, left right
def gen_css_image_properties():
    random_z_index = random.randint(0, 5)
    random_number = random.randint(0, 7)
    css_string = "style='position: absolute; z-index: " + str(random_z_index) + ";"
    if random_number > 1 and random_number < 5:
        left = random.randint(0, 75)
        css_string = css_string + " left: " + str(left) + "%;"
    if random_number >= 3:
        right = random.randint(0,75)
        css_string = css_string + " right: " + str(right) + "%;"
    if random_number < 2:
        top = random.randint(0,95)
        css_string = css_string + " top: " + str(top) + "%;"
    if random_number % 2 == 0:
        bottom = random.randint(0, 95)
        css_string = css_string + " bottom: " + str(bottom) + "%;"
    return css_string + "'"


# generate max_width for images and return a css string
def gen_max_width_for_images(css_string):
    max_width = random.randint(100, 500)
    max_width_css = "max-width: "
    css_with_max_width = css_string[0:7] + max_width_css + str(max_width) + "px; "
    return css_with_max_width + css_string[7:]


# generate complete image tag for static asset by concatenating results from generate_static_assets()
# and generate_css_image_properties()
def gen_complete_image_tag(static_asset, css_string):
    html_string = static_asset
    css = css_string

    # insert generated css into image tag
    html_string = html_string[:5] + css + html_string[4:]
    return html_string


# generate random asset using all functions
def gen_asset():
    return gen_complete_image_tag(gen_static_assets(), gen_max_width_for_images(gen_css_image_properties()))


# generate css values for web page, takes background_image argument passed by generate_background()
# and assigns random font from font_matrix
def gen_css_body_properties(background_image):
    background = background_image
    font_family = "'Times New Roman', sans-serif"
    random_number = random.randint(0, 2)
    css_string = "body { \nwidth: 100%;\ntext-align: center;\n"
    font_face_css = "}\n@font-face { \nfont-family: '"

    css_string = css_string + background + ";"

    if random_number == 2:
        css_string = css_string + "\nfont-family: " + font_family + ";"
    elif random_number == 0:
        font_family = font_matrix.fonts[0][0]
        font_source = font_matrix.fonts[0][1]
        font_face_css = font_face_css + font_family + "; src: url('" + font_source + "');"
        css_string += font_face_css
    else:
        font_family = str(font_matrix.fonts[random_number][0])
        font_source = str(font_matrix.fonts[random_number][1])
        font_face_css = font_face_css + font_family + "'; src: url('" + font_source + "');"
        css_string += font_face_css
    return css_string


# generate a css property and return it in a div
def gen_css_div_properties():
    div_css = "#centerContainer {\nwidth: 900px; \ntext-align: left; \nmargin: 0 auto;}"
    return div_css


# enclose the css string in <style> tags
def gen_page_css():
    open_css = "<style type='text/css'>\n"
    close_css = "\n</style>"
    return open_css + gen_css_body_properties(gen_background()) + "\n} \n" + gen_css_div_properties() + close_css


# generate paragraphs using the faker library and enclose in <p> tags
def gen_paragraphs():
    random_sentence = ""
    for sentence in range(0, 6):
        random_sentence += fake.text()
    return '<p>' + random_sentence + '</p>'
