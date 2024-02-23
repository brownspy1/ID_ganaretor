import pdfkit


def create_pdf(html_content, output_path):
    pdfkit.from_string(html_content, output_path)


if __name__ == "__main__":
    # Read your HTML template
    with open("IDCard.html", "r+", encoding="utf-8") as file:
        html_content = file.read()

    # Modify HTML content with dynamic data if needed
    # For example, you can use string formatting to replace placeholders with actual data

    # Output path for the generated PDF file
    output_path = "id_card.pdf"

    # Generate PDF
    create_pdf(html_content, output_path)
