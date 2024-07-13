from weasyprint import HTML, CSS
from jinja2 import Template
import os
from data import data


template_path = "./britam_ug/index.html"
css_template_path = "./britam_ug/css/style.css"
pdf_path = "./britam_ug/sample_letter.pdf"

image_path = os.path.abspath("./britam_ug/images/uap_holdings.png")


# Load HTML template
with open(template_path) as file:
    template = Template(file.read())
with open(css_template_path) as file:
    css_content = file.read()
# Sample data
# data = {"image_path": image_path}

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
