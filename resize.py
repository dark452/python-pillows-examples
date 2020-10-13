from PIL import Image

if __name__ == "__main__":
    try:
        image = Image.open('images/flores.jpg')
        width, height = image.size
        #resize de imagenes:
        #tupla debe contener numeros enteros
        new_width = width // 5
        new_height = height // 5

        resize = image.resize((new_width,new_height))
        resize.show()
    except FileNotFoundError as error:
        print("El archivo no se encuentra :( !")