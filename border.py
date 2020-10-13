from PIL import Image
from PIL import ImageOps


if __name__ == "__main__":
    
    try:
        image = Image.open('images/flores.jpg')
        image = ImageOps.expand(
                image,
                border=(30,20,30,20), #tupla top,right,bottom,left
                fill=(190,190,250)
            )
        image.show()

        #new_image.show()
       

    except FileNotFoundError as err:
        print("No se puede cargar la imagen")