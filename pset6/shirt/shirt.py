import sys
import os
from PIL import Image, ImageOps

def main():
    # Check if exactly two command-line arguments are provided
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 3 else "Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        sys.exit("Input does not exist")

    # Validate file extensions
    valid_extensions = ('.jpg', '.jpeg', '.png')
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid output")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    # Open the input image and shirt overlay
    input_image = Image.open(input_file)
    shirt_image = Image.open("shirt.png")

    # Resize and crop the input image to fit the shirt
    resized_image = ImageOps.fit(input_image, shirt_image.size)

    # Overlay the shirt on the resized image
    resized_image.paste(shirt_image, (0, 0), shirt_image)

    # Save the output image
    resized_image.save(output_file)

if __name__ == "__main__":
    main()
