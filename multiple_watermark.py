from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

FONT_PATH = "fonts/Roboto/Roboto-BoldItalic.ttf"
FONT_SIZE = 20
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
        text_size = draw.textsize(MESSAGE, font=font)

        for pos_x in range(0, image.size[0], text_size[0] + 20):
            for pos_y in range(0, image.size[1], text_size[1] + 50):
                draw.text(
                    (pos_x, pos_y),
                    MESSAGE,
                    (255,255,255,50),
                    font=font
                )

     
        #new_image.show()
        water_mark = Image.alpha_composite(image,new_image)
        water_mark.show()

    except FileNotFoundError as err:
        print("No se puede cargar la imagen")