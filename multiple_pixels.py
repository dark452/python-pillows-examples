from PIL import Image

if __name__ == "__main__":
    try:
        image = Image.open('images/flores.jpg')

        print(image.size)  #tupla con el ancho y alto
        width, height = image.size
        #usaremos el método getdata y getpixel

        pixeles = image.getdata()  #listado de tuplas con los pixeles de la imagen

        #cantidad de pixeles que tiene la imagen
        print(len(pixeles))

        #iteramos sobre la lista de pixeles

        #for pixel in pixeles:
            #print (pixel)
        
        #image.show()
        #list comprehension, quitamos rojo y azul al rgb para ver los cambios
        new_pixeles = [
            (0,pixel[1],0) #almacenaremos tuplas (r,g,b) en este caso almacenaremos valores originales
            for pixel in pixeles
        ]   

        #método putdata modifica la imagen, en este caso mandamos por parametros el listado con los pixeles originales
        image.putdata(new_pixeles)
        image.show()
    except FileNotFoundError as error:
        print("El archivo no se encuentra :( !")