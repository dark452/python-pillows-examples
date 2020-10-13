from PIL import Image

if __name__ == "__main__":
    try:
        image = Image.open('images/flores.jpg')

        ###crop se require 4 int en una tupla (left, upper, right, lower)
        cropped = image.crop((200,100,400,300))
        cropped.show()
        cropped.save('images/flor.jpg')
        #image.show()
    except FileNotFoundError as error:
        print("El archivo no se encuentra :( !")