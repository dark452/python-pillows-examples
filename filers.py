from PIL import Image
from PIL import ImageFilter

if __name__ == "__main__":
    try:
        image = Image.open('images/flores.jpg')

        print(image.size)  #tupla con el ancho y alto
        width, height = image.size

        #usaremos el filtro blur
        filter = ImageFilter.GaussianBlur(radius=20)
        filtrada = image.filter(filter)

        filtrada.show()
      
        #image.show()
    except FileNotFoundError as error:
        print("El archivo no se encuentra :( !")