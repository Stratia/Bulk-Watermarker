import os
from PIL import Image

def Watermark():
    global background,watermark_image
    watermark = os.listdir(fr'Watermark')
    value = 0
    for index in os.listdir('images'):
        print(index)
        background = Image.open(fr"images\{index}")
        watermark_image = Image.open(fr"Watermark\{watermark[0]}")

        width = watermark_image.width
        height = watermark_image.height

        water = watermark_image.resize((width, height), )  # Width-Height

        background.paste(water, (background.width - width, background.height - height), water)  # X-Y

        background.save(rf'Outcome\outcome{value}.png', quality=95)
        value+=1

Watermark()