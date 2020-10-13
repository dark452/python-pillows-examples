from PIL import Image

if __name__ == "__main__":
    try:
        image = Image.open('images/flores.jpg')

        print(image.size)  #tupla con el ancho y alto
        width, height = image.size
        #to get the pixel we use the getpixel method, which parameter is a tuple with (x,y)

        pixel = image.getpixel((0,0))
        #return the RGB's pixel, be aware that the RGB it's only if is a JPG image, if is a PNG
        #it will also return a 4th value called alpha
        print(pixel)
        #get the values from the tuple
        red, green, blue = pixel
        print("RED ", red)
        print("GREEN ", green)
        print("BLUE ", blue)

        #modify a pixel, use the putpixel method (it modify the original image)
        #putpixel method recieve 2 tuples ((x,y) , (R,G,B))

        #image.putpixel(
        #    (0,0),
        #    (255,255,255)
        #)
      
        #image.show()

        #to modify a rectangle
        for posx in range(0, 200):
            for posy in range(0, 300):
                image.putpixel(
                (posx,posy),
                (255,255,255)
                )
        
        image.show()
            

    except FileNotFoundError as error:
        print("El archivo no se encuentra :( !")