from weasyprint import HTML, CSS
from jinja2 import Template


template_path = "./britam/index.html"
css_template_path = "./britam/css/style.css"
pdf_path = "./britam/sample_letter.pdf"

# Load HTML template
with open(template_path) as file:
    template = Template(file.read())
with open(css_template_path) as file:
    css_content = file.read()
# Sample data
data = {}

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
