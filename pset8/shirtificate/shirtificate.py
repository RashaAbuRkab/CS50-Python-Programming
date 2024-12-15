from fpdf import FPDF

# Define a class that extends FPDF
class ShirtificatePDF(FPDF):
    def header(self):
        # Add the title "CS50 Shirtificate" at the top
        self.set_font("Arial", "B", 24)
        self.cell(0, 20, "CS50 Shirtificate", ln=True, align="C")

    def add_shirt_image(self, image_path):
        # Set x and y positions to center the image
        self.image(image_path, x=0, y=60, w=210)

    def add_name(self, name):
        # Set the font and size for the name text
        self.set_font("Arial", "B", 30)
        self.set_text_color(255, 255, 255)  # White color
        self.text(x=60, y=140, txt=name)

# Prompt the user for their name
name = input("What's your name? ")

# Create a new PDF object
pdf = ShirtificatePDF(orientation="Portrait", format="A4")

# Add a page to the PDF
pdf.add_page()

# Add the shirt image to the PDF
pdf.add_shirt_image("shirtificate.png")

# Add the user's name on top of the shirt
pdf.add_name(name)

# Output the PDF to a file
pdf.output("shirtificate.pdf")

print("PDF generated successfully!")
