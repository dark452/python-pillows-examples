from PIL import Image

if __name__ == "__main__":
    try:
        image = Image.open('images/flores.jpg')

        bands = image.getbands()
        print(bands)
       
        #para trabajar con las bandas se usa el método split
        red, green ,blue = image.split() # tupla (r,g,b,a)

        print("RED ", red)
        print("GREEN ", green)
        print("BLUE ", blue)
        red.show()
        green.show()
        blue.show()
      
      
        #image.show()
    except FileNotFoundError as error:
        print("El archivo no se encuentra :( !")