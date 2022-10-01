from PIL import Image

file = input("Enter image filename with extension:")
image = Image.open(file)
pixels = image.load()

out_file = open("output.bin", "wb")

vertical = input("Enter vertical pixel amount:")
horizontal = input("Enter horizontal pixel amount:")

for y in range(vertical):
    for x in range(horizontal):
        try:
          out_file.write(chr(pixels[x, y]))
        except IndexError:
            out_file.write(chr(0))
