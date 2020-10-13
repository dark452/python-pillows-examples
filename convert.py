from PIL import Image

if __name__ == "__main__":
    try:
        image = Image.open('images/flores.jpg')

        blanco_negro = image.convert('L')
        blanco_negro.show()
        blanco_negro.save('images/flores_blanco_negro.jpg')
        #image.show()
    except FileNotFoundError as error:
        print("El archivo no se encuentra :( !")