import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)
    elif len(sys.argv) == 3:
        # Two arguments: check for the correct format
        if sys.argv[1] in ("-f", "--font"):
            font = sys.argv[2]
            if font in figlet.getFonts():
                figlet.setFont(font=font)
            else:
                print(f"Error: '{font}' is not a valid font.", file=sys.stderr)
                sys.exit(1)
        else:
            print("Usage: python figlet.py [-f | --font] font_name", file=sys.stderr)
            sys.exit(1)
    else:
        print("Usage: python figlet.py [-f | --font] font_name", file=sys.stderr)
        sys.exit(1)

    # Prompt user for text input
    text = input("Text: ")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
