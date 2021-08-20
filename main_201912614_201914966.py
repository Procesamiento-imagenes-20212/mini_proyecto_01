import os
import shutil
import glob
import cv2
import matplotlib.pyplot as plt


def abrir_imagen(ruta):
    return cv2.imread(ruta)


def es_elefante(num_imagen):
    handle_gt1 = open(os.path.join("data_mp1", "elephants_dataset", "gt1", "gt1.csv"))
    linea = handle_gt1.readline()
    while len(linea) > 0:
        if not num_imagen in linea:
            linea = handle_gt1.readline()
            continue
        booleano = True if not "Non" in linea.split(",")[1] else False
        texto = "Elefante" if booleano else "No elefante"
        handle_gt1.close()
        return texto


def cargar_imagenes(numero=1):
    while True:
        imagen_principal = input("Ingrese la imagen {} a cargar: ".format(numero))
        if not "." in imagen_principal:
            imagen_principal += ".jpg"
        print("Cargando imagen {}...\n".format(numero))
        original = abrir_imagen(os.path.join("data_mp1", "elephants_dataset", "imgs", imagen_principal))
        gt1 = es_elefante(imagen_principal)
        gt2 = abrir_imagen(os.path.join("data_mp1", "elephants_dataset", "gt2", imagen_principal))
        gt3 = abrir_imagen(os.path.join("data_mp1", "elephants_dataset", "gt3", imagen_principal))
        try:
            if len(original) > 0:
                print("La imagen {} fue cargada correctamente".format(numero))
                return original, gt1, gt2, gt3
        except:
            print("La imagen {} no fue cargada".format(numero))
            continue


def punto_elefantes():
    set_imagen_1 = cargar_imagenes()
    set_imagen_2 = cargar_imagenes(2)

    input("\nPresione enter para generar gráfico...")
    for i in range(8):
        plt.subplot(2, 4, i + 1)
        if i == 0:
            plt.title("Imagenes originales")
            plt.imshow(set_imagen_1[0])
        if i == 1:
            plt.title("Clasificación")
            plt.text(0.25, 0.5, s=set_imagen_1[1], fontsize=15)
        if i == 2:
            plt.title("Detección")
            plt.imshow(set_imagen_1[2])
        if i == 3:
            plt.title("Segmentación")
            plt.imshow(set_imagen_1[3])
        if i == 4:
            plt.imshow(set_imagen_2[0])
        if i == 5:
            plt.text(0.25, 0.5, s=set_imagen_2[1], fontsize=15)
        if i == 6:
            plt.imshow(set_imagen_2[2])
        if i == 7:
            plt.imshow(set_imagen_2[3])
        plt.xticks([])
        plt.yticks([])
    plt.show()

    input("Presione enter para continuar...")


def iniciar():
    while True:
        print("\n1- Punto elefantes\n2- Aplicacion_biomedica\n3- Salir")
        op = input("\nSeleccione opción a utilizar: ")
        if op == "1":
            punto_elefantes()
        elif op == "3":
            break
        else:
            print("\nSeleccione una opción válida")


iniciar()