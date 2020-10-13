from PIL import Image

if __name__ == "__main__":
    try:
        image = Image.open('images/muertos.png')

        #new_list = list() #lista para guardar los pixeles

        #for pixel in image.getdata():
            #tupla (r,g,b,a)
         #   if pixel[3] == 0:
         #       new_list.append((194,113,208))
         #   else:
         #       new_list.append(pixel)
        
        ##mismo codigo pero con list comprehensions
        new_list = [
            (194,113,208) if pixel[3] == 0 else pixel
            for pixel in image.getdata()
        ]

        image.putdata(new_list)
        image.show()
    except FileNotFoundError as error:
        print("El archivo no se encuentra :( !")