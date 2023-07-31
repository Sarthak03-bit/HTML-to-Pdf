import pdfkit
import os

# Set the path to the wkhtmltopdf executable on your system
# Replace '/path/to/wkhtmltopdf' with the actual path
path_to_wkhtmltopdf = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'

def generate_certificate(name, course, date):
    # Read the content of the certificate.html file
    with open('certificate.html', 'r') as file:
        html_template = file.read()

    # Replace placeholders with actual values in a copied version
    html_output = html_template.replace('{{name}}', name)
    html_output = html_output.replace('{{course}}', course)
    html_output = html_output.replace('{{date}}', date)

    # Configure options for PDF generation
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        'quiet': '',
        'no-outline': None
    }

    # Specify the output path for the PDF in the same directory as the script
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'certificate2.pdf')

    # Convert the HTML to PDF using pdfkit and specify the path to wkhtmltopdf
    pdfkit.from_string(html_output, output_path, options=options, configuration=pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf))

# Example usage
name = "John Doe"
course = "Python Programming"
date = "2023-07-31"
generate_certificate(name, course, date)
