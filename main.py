import generate
from random import randint


# main function that calls all functions in generate.py and returns an html string
def build_web_page():
    page_title = generate.gen_title()
    page_title_html = "<title>" + generate.gen_title() + "</title>"
    header_title = page_title
    page_css = generate.gen_page_css()
    static_assets_html = ""
    random_number_assets = randint(7,15)
    counter = 0

    while counter < random_number_assets:
        static_assets_html = static_assets_html + generate.gen_asset() + "\n"
        counter += 1

    counter_2 = 0
    random_number_assets_2 = randint(4, 7)

    while counter_2 < random_number_assets_2:
        static_assets_html = static_assets_html + generate.gen_paragraphs() + "\n"
        counter_2 +=1

    header_title_html = "<h1 style='z-index: 300; position: relative; background: #fff;'>" + header_title + "</h1>"

    html_open = "<!DOCTYPE html>\n<html>\n"
    html_close = "\n</html>"
    head = "<head>\n" + page_title_html + "\n" + page_css + "\n</head>\n"
    body = "<body>\n" + header_title_html + "\n<div id='centerContainer'>\n" + static_assets_html + "\n</div>\n</body>"

    # placeholder for generating random body text
    return html_open + head + body + html_close


# creates file called index.html and inserts returned value from build_web_page()
def write_to_file():
    file_name = "index.html"
    file = open(file_name, 'w')
    file.write(build_web_page())

# main loop
write_to_file()
