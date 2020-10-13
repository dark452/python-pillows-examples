from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

BACKGROUND_COLOR = (95, 200, 245)
SIZE = (1920,1080)
MESSAGE = "RedeshostCL"

if __name__ == "__main__":
    try:
        image = Image.new(
            'RGB',
            SIZE,
            BACKGROUND_COLOR
        )

        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('fonts/Roboto/Roboto-Bold.ttf',200)

        #para encontrar el tamaño del texto:
        width,heigh = draw.textsize(MESSAGE, font=font)

        print(width)
        print(heigh)

        #coordenadas (tupla), texto y color (tupla), fuente
        draw.text(
            (SIZE[0] // 2 - width // 2, SIZE[1] // 2 - heigh // 2),
            MESSAGE,
            (255,255,255),
            font=font
        )

        #para tener una copia exacta de la imagen original
        copia = image.copy()
      
        #para crear un thumbnail, el métedo recibe una tupla con el tamaño máximo del thumbnail

        copia.thumbnail((500,500))
        copia.show()
        image.show()


    except FileNotFoundError as error:
        print("El archivo no se encuentra :( !")