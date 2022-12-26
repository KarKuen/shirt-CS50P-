import sys
from PIL import Image, ImageOps

def main():
    two()
    input = sys.argv[1].lower()
    output = sys.argv[2].lower()
    filetype(input, output)
    samefiletype(input, output)
    try:
        editimage()
    except FileNotFoundError:
        sys.exit()


def two():
    if len(sys.argv) == 3:
        return(True)

    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    else:
        sys.exit('Too few command-line arguments')

def filetype(input, output):
    if input.endswith('.jpg') or input.endswith('.jpeg') or input.endswith('.png'):
        if output.endswith('.jpg') or output.endswith('.jpeg') or output.endswith('.png'):
            return(True)
        else:
            sys.exit('Invalid input')
    else:
        sys.exit('Invalid input')

def samefiletype(input, output):
    endi = input.find('.')
    endo = output.find('.')

    if input[endi:] == output[endo:]:
        return(True)
    else:
        sys.exit('Input and output have different extensions')

def editimage():
    with Image.open (sys.argv[1]) as image:
            shirt = Image.open('shirt.png')
            size = shirt.size
            image = ImageOps.fit(image, size)
            image.paste(shirt, shirt)
            image.save(sys.argv[2])

main()