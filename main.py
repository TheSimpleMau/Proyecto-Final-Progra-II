#######################################
###Importando los modulos necesarios###
#######################################

#Importamos la clase Plots que crea los textos en Latex
from Plots import *
#Importamos la clase WebScraping que realiza el scraping de la pagina
from WebScraping import *
#Importamos el modulo tkinter para crear una interfaz bonita uwu
from tkinter import *
from tkinter import messagebox
#Del modulo time, importamos sleep
from time import sleep

########################
###Programa principal###
########################
bg = '#0e108f'

ventana = Tk()
ventana.title("FomuYA")
ventana.configure(background=bg,padx=50,pady=50)


def busqueda(a_buscar,archivo_txt):
    #Obtenemos las formulas de wikipedia
    scrap = GetFormulas(a_buscar,archivo_txt)
    #Para cada formula, generamos un png que será la ecuacion en latex
    for formula in scrap.math_formulas:
        Plots(formula,a_buscar)
    #Por último, como existe un error entre los modulos de tkinter y matplotlib,
    #ejecutamos desde la terminal el archivo Display que nos muestra los png
    #generados.
    os.system('python3 Display.py')

#Definimos una funcion que guie al usuario en el programa
def ayuda():
    messagebox.showinfo("Ayuda", """Este programa busca las formulas de una ecuacion en wikipedia y las genera en formato latex
Para realizar la busqueda, escriba el nombre de la ecuacion en la caja de texto y presione el boton buscar.
Si así lo desea, puede guardar todas las ecuciones en un archivo txt. Las ecuaciones estan escritas en formato latex.
El programa puede tardar en buscar y/o generar las imagenes, así que no se preocupe si se llega a trabar""")

#Etiqueta para el titulo
Titulo_etiqueta = Label(ventana, text="Programa facherito 😎", font=("Arial", 40), bg=bg)
Titulo_etiqueta.grid(row=0, column=0, columnspan=3)

#Etiqueta para señalar la parte de busqueda
busqueda_etiqueta = Label(ventana, text="Ingresa la formula/ecuación\nó tema a buscar: ",font=("Arial", 20), bg=bg)
busqueda_etiqueta.grid(row=1, column=0)

#Caja de texto para ingresar la busqueda
busqueda_texto = Entry(ventana, width=50)
busqueda_texto.grid(row=1, column=1, columnspan=2)

#Etiqueta para indicar si se quiere guardar en un archivo txt
archivo_txt_etiqueta = Label(ventana, text="¿Desea generar un archivo .txt con\ntodos los archivos que encuentre?: ",font=("Arial", 20),bg=bg)
archivo_txt_etiqueta.grid(row=2, column=0)

#Spinbox para indicar si se quiere guardar en un archivo txt
archivo_txt_spinbox = Spinbox(ventana, values=('No','Si'), width=10,font=("Arial", 20),highlightthickness=0)
archivo_txt_spinbox.grid(row=2, column=1)

#Boton de buscar
buscar_boton = Button(ventana, text="Buscar", command=lambda: busqueda(busqueda_texto.get(),archivo_txt_spinbox.get()),font=("Arial", 20), bg=bg,highlightthickness=0)
buscar_boton.grid(row=1, column=3,columnspan=2)

#Boton de ayuda
boton_ayuda = Button(ventana, text="Ayuda", command=lambda: ayuda(),font=("Arial", 20), bg=bg,highlightthickness=0)
boton_ayuda.grid(row=3, column=0)

#Boton de salir
boton_salida = Button(ventana, text="Salir", command=ventana.destroy,font=("Arial", 20), bg=bg,highlightthickness=0)
boton_salida.grid(row=3, column=3)

#Bucle para que el programa se mantiene en ejecucion
ventana.mainloop()