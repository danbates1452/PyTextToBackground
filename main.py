from nltk import word_tokenize
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import textwrap


with open('beemovie.txt', 'r') as file:
    data = file.readlines()
    print(len(data))
    lines = [word.upper() for line in data for word in word_tokenize(line) if word.isalpha()]
    print(len(lines))
    print(lines)
    text = "".join(lines)

text = textwrap.wrap(text, 300)

img = Image.new(mode="RGB", size=(1920, 1080))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Raleway/static/Raleway-Regular.ttf", 10)
height = 0
for i in range(0, len(text)):
    draw.text((0, height), text[i], (255, 255, 0), font=font)
    height = height + 10

img.save("beemovie-bg.png")
