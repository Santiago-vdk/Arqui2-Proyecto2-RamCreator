import numpy as np
import cv2
from bitstring import BitArray

while(1):
    print("Digite 1 para crear MIF ")
    print("Digite 'q' para cerrar la ejecucion")
    opcion = input("Opcion: ")
    if(opcion == "q"):
        break
    elif(int(opcion) == 1):
        img = input("Digite el nombre de su imagen: ")
        if(img == "q"):
            break

        print("Creando archivo MIF...")
        image = cv2.imread(img)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resize = cv2.resize(image_gray, (100, 100))

        cv2.imwrite('Output/resize_' + img, resize)
        cv2.imwrite('Output/output_' + img, resize)
        output = cv2.imread('output_' + img)

        f = open("Output/RAM.mif", "w+")

        f.write("WIDTH = 32;")
        f.write("\n")
        f.write("DEPTH = 16383;")
        f.write("\n")
        f.write("\n")

        f.write("ADDRESS_RADIX = UNS;")
        f.write("\n")
        f.write("DATA_RADIX = BIN;")
        f.write("\n")
        f.write("\n")
        f.write("CONTENT BEGIN")
        f.write("\n")

        i, j, k = 0, 0, 0

        height, width = resize.shape[:2]

        while(i < height):
            while(j < width):
                px_1 = resize[i, j]
                px_2 = resize[i, j + 1]
                px_3 = resize[i, j + 2]
                px_4 = resize[i, j + 3]

                px_1 = str(bin(px_1)[2:].zfill(8))
                px_2 = str(bin(px_2)[2:].zfill(8))
                px_3 = str(bin(px_3)[2:].zfill(8))
                px_4 = str(bin(px_4)[2:].zfill(8))

                pixels = px_4 + px_3 + px_2 + px_1
                f.write("\t")
                f.write(str(k) + " : " + pixels + ";")
                f.write("\n")

                j += 4
                k += 1
            i += 1
            j = 0

        f.write("\t")
        f.write("[" + str(k) + ".." + str(16383) + "]" +
                " : " + str(bin(0)[2:].zfill(32)) + ";")
        f.write("\n")
        f.write("END;")
        f.close()

        print("Listo!")
        print("------------------------------------------")
