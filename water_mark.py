from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

FONT_PATH = "fonts/Roboto/Roboto-BoldItalic.ttf"
FONT_SIZE = 80
MESSAGE = "RedeshostCL"

if __name__ == "__main__":
    
    try:
        image = Image.open('images/flores.jpg')
        image = image.convert('RGBA')
        #crearemos una nueva imagen
        new_image = Image.new('RGBA' , image.size, (255,255,255,0))
        #convertir imagen a png
        
        font = ImageFont.truetype(FONT_PATH,FONT_SIZE)

        draw = ImageDraw.Draw(new_image)
        #para encontrar el tamaño del texto:
        width,heigh = draw.textsize(MESSAGE, font=font)
        draw.text(
            (new_image.size[0] // 2 - width // 2, new_image.size[1] // 2 - heigh // 2),
            MESSAGE,
            (255,255,255,50),
            font=font
        )

     
        #new_image.show()
        water_mark = Image.alpha_composite(image,new_image)
        water_mark.show()

    except FileNotFoundError as err:
        print("No se puede cargar la imagen")