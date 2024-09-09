from weasyprint import HTML, CSS
from jinja2 import Template
import os

# from data import data


template_path = "./indico/index.html"
css_template_path = "./indico/css/style.css"
pdf_path = "./indico/sample_report.pdf"

# image_path = os.path.abspath("./britam_ug/images/uap_holdings.png")


# Load HTML template
with open(template_path) as file:
    template = Template(file.read())
with open(css_template_path) as file:
    css_content = file.read()
# Sample data
data = {
    "intermediary_logo": "https://www.wiseseguros.co.mz/img/logo.svg",
    "company_logo": "https://www.wiseseguros.co.mz/img/logo.svg",
    "ai_images": [
        {
            "original_image": "https://images.pexels.com/photos/24778766/pexels-photo-24778766/free-photo-of-scenic-view-of-mountains-in-iceland.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "ai_image": "https://images.pexels.com/photos/24778766/pexels-photo-24778766/free-photo-of-scenic-view-of-mountains-in-iceland.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "name": "FrontSide",
            "damages": {"tailgate": ["scratch"], "back_bumper": ["scratch"]},
        },
        {
            "original_image": "https://images.pexels.com/photos/24778766/pexels-photo-24778766/free-photo-of-scenic-view-of-mountains-in-iceland.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "ai_image": "https://images.pexels.com/photos/24778766/pexels-photo-24778766/free-photo-of-scenic-view-of-mountains-in-iceland.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "name": "FrontSide",
            "damages": {"tailgate": ["scratch"], "back_bumper": ["scratch"]},
        },
        {
            "original_image": "https://images.pexels.com/photos/24778766/pexels-photo-24778766/free-photo-of-scenic-view-of-mountains-in-iceland.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "ai_image": "https://images.pexels.com/photos/24778766/pexels-photo-24778766/free-photo-of-scenic-view-of-mountains-in-iceland.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "name": "FrontSide",
            "damages": {"tailgate": ["scratch"], "back_bumper": ["scratch"]},
        },
    ],
}

html_output = template.render(data)

# options = {
#     'page-size': 'Letter',
#     'margin-top': '0mm',
#     'margin-right': '0mm',
#     'margin-bottom': '0mm',
#     'margin-left': '0mm',
# }


# HTML(string=html_output).write_pdf("report_sample_doc.pdf")

html = HTML(string=html_output)
css = CSS(string=css_content)
html.write_pdf(pdf_path, stylesheets=[css])
