from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

SIZE = (1920,1080)
BACKGROUND_COLOR = (237, 94, 196)
MESSAGE = "Aprende \nPython!"
FONT_COLOR = (255,255,255)
POS_X = 100
POS_Y = 200

if __name__ == "__main__":
    
    try:
        image = Image.new(
            'RGBA',
            SIZE,
            BACKGROUND_COLOR

        )

        python_logo = Image.open("images/python.png").convert('RGBA')
        redeshost_logo = Image.open("images/redeshost.png")
        #print(python_logo.mode)
        #ahora pegamos el logo en la imagen principal
        image.paste(python_logo, (1200,POS_Y), mask=python_logo)
        image.paste(redeshost_logo, (POS_X,950), mask=redeshost_logo)
        
        font = ImageFont.truetype('fonts/Roboto/Roboto-Medium.ttf',160)
        draw = ImageDraw.Draw(image)

        draw.text(
            (POS_X,POS_Y),
            MESSAGE,
            FONT_COLOR,
            font=font
        )

        image.thumbnail(
            image.size
        )
        image.show()
       

        #new_image.show()
       

    except FileNotFoundError as err:
        print("No se puede cargar la imagen")