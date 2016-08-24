import generate
from random import randint


def build_web_page():
    page_title = generate.gen_title()
    page_css = generate.gen_page_css()
    static_assets_html = ""
    random_number_assets = randint(7,50)
    counter = 0

    while counter < random_number_assets:
        static_assets_html = static_assets_html + generate.gen_asset() + "\n"
        counter += 1

    counter_2 = 0
    random_number_assets_2 = randint(1, 7)

    html_open = "<!DOCTYPE html>\n<html>\n"
    html_close = "\n</html>"
    head = "<head>\n" + page_title + "\n" + page_css + "\n</head>\n"
    body = "<body>\n<div id='centerContainer'>\n" + static_assets_html + "\n</div>\n</body>"

    # placeholder for generating random body text

    return html_open + head + body + html_close


def write_to_file():
    file_name = "index.html"
    file = open(file_name, 'w')
    file.write(build_web_page())

write_to_file()
