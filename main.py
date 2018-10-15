import numpy as np
import cv2
from bitstring import BitArray


while(1):
    print("Digite 1 para crear MIF ")
    print("Digite 2 para reconstruir imagen")
    print("Digite 'q' para cerrar la ejecucion")
    opcion= input("Opcion: ")
    if(opcion == "q"):
            break
    elif(int(opcion) == 1):
        img = input("Digite el nombre de su imagen: ")
        if(img == "q"):
            break

        print("Creando archivo MIF...")
        image = cv2.imread(img)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resize = cv2.resize(image_gray, (150,150)) 

        cv2.imwrite('resize.jpg', resize)
        cv2.imwrite('output.jpg', resize)
        output = cv2.imread('output.jpg')

        f = open("RAM.mif","w+")
        
        f.write("WIDTH = 8;")
        f.write("\n")        
        f.write("DEPTH = 65536;")
        f.write("\n")
        f.write("\n")
        
        f.write("ADDRESS_RADIX = UNS;")
        f.write("\n")
        f.write("DATA_RADIX = BIN;")
        f.write("\n")
        f.write("\n")
        f.write("CONTENT BEGIN")
        f.write("\n")

        i,j,k = 0,0,0
        filtro = [0,0,0,0,1,0,0,0,0]
        
        #for x in filtro:
            
        #    f.write("\t")
        #    f.write(str(k) + " : " + str( bin(x & 0xff)[2:].zfill(8) ) + ";")
        #    f.write("\n")
        #    k += 1

        height, width = resize.shape[:2]
        
        while(i<height):
            while(j<width):
                px = resize[i,j]
                f.write("\t")
                f.write(str(k) + " : " + str(bin(px)[2:].zfill(8)) + ";")
                f.write("\n")
               # output[i,j] = int(bin(px)[2:].zfill(8),2) + 100
                j += 1
                k += 1
            i += 1
            j = 0

       

        f.write("\t")
        f.write("[" + str(k) + ".." + str(63536 - 1) + "]" + " : " + str(bin(0)[2:].zfill(8)) + ";")
        f.write("\n")
        f.write("END;")
        f.close()

        cv2.imwrite('output.jpg', output)
        print("Listo!")
        print("------------------------------------------")
    elif(int(opcion) == 2):
        print("Cargando volcado de memoria")
        print("------------------------------------------")
