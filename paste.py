from PIL import Image

if __name__ == "__main__":
    try:
        flores = Image.open('images/flores.jpg')

        flor = Image.open('images/flor.jpg')
        #pegar una imagen sobre otra
        #paste el método paste, SI MODIFICA LA IMAGEN ORIGINAL
        flores.paste(
            flor,
            (500,150) #2 int (x , y)
        )
        flores.show()
        #image.show()
    except FileNotFoundError as error:
        print("El archivo no se encuentra :( !")