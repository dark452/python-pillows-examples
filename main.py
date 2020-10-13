from PIL import Image

if __name__ == "__main__":
    try:
        image = Image.open('images/flores.jpg')

        print(image.size)  #tupla con el ancho y alto
        width, height = image.size
        print("Ancho ",width)
        print("Alto ", height)
        print( image.mode)
        print(image.format)
      
      
        #image.show()
    except FileNotFoundError as error:
        print("El archivo no se encuentra :( !")