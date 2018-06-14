# Opens all.csv and saves the date to visualization.png

from PIL import Image

def color(scalar):
    # Creates a greyscale colour from a scalar 0-15
    v = int(float(scalar) / 15 * 256)
    return (v, v, v)

def main():
    pixels = []

    with open("all.txt", "r") as file:
        for line in file:
            value_from, value_to, method, method_length = line.split(",")
            pixel = tuple(map(int, [value_from, value_to, method_length]))
            pixels.append(pixel)

    img = Image.new("RGB", (256, 256))

    for pixel in pixels:
        img.putpixel((pixel[0], pixel[1]), color(pixel[2]))

    img.save("visualization.png")
	
if(__name__ == "__main__"):
    main()
