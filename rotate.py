from PIL import Image

if __name__ == "__main__":
    try:
        image = Image.open('images/flores.jpg')

        #METODO CON NUMEROS para rotar
        rotada_1 = image.rotate(45, expand=True)
        
        #rotar con constantes
        #Image.ROTATE_90
        #Image.ROTATE_180
        #Image.ROTATE_270
        rotada_2 = image.transpose(Image.ROTATE_90)
        
        rotada_1.show()
        rotada_2.show()
        #image.show()
    except FileNotFoundError as error:
        print("El archivo no se encuentra :( !")