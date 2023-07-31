
import pdfkit
import html


def generate_certificate(name, course, date):
    with open("certificate.html", "r") as f:
        html_content = f.read()

    # Replace the placeholders
  
    html_content = html_content.replace("{{name}}", name)
    html_content = html_content.replace("{{course}}", course)
    html_content = html_content.replace("{{date}}", date)

    # Convert the HTML content to PDF
    pdfkit.from_string(html_content, "certificate.pdf")


if __name__ == "__main__":
    name = "Sarthak"
    course = "Python Programming"
    date = "2023-07-31"

    generate_certificate(name, course, date)
