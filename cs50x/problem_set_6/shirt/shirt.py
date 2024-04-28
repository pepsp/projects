from PIL import Image, ImageOps
from os.path import splitext
import sys

def main():
    try:
        input, output = command_check(sys.argv)
        get_input(input, output)

    except ValueError as ve:
        print(ve)
        sys.exit(1)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    except IndexError as ie:
        print(ie)
        sys.exit(1)

def command_check(argv):
    if  len(argv) == 3 and splitext(argv[1])[1] != splitext(argv[2])[1]:
        raise ValueError("Input and output have different extensions")
    else:
        if len(argv) < 3:
            raise IndexError("Too few command-line arguments")
        elif len(argv) > 3:
            raise IndexError("Too many command-line arguments")
        elif len(argv) == 3 and splitext(argv[1])[1] == splitext(argv[2])[1] and argv[1].endswith((".jpg",".jpeg",".png")):
            return argv[1], argv[2]
        else:
            raise ValueError("Not an image file")

def get_input(input, output):
    shirt = Image.open("shirt.png")
    size = shirt.size
    input_image = Image.open(input)
    muppet = ImageOps.fit(input_image, size)
    muppet.paste(shirt, shirt)
    muppet.save(output, splitext(output[1])[1].lower())



if __name__ == "__main__":
    main()

