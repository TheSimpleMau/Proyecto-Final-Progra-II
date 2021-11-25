#######################################
###Importando los modulos necesarios###
#######################################

#Importamos pyplot de matplotlib
import matplotlib.pyplot as plt
#Importamos os
import os


#Clase para graficar
class Plots:

    #Constructor de la clase, se le pasa el texto en LaTeX de la ecuacion y la busqueda realizada
    def __init__(self,text,busqueda) -> None:
        #Guardamos el texto en LaTeX
        self.text = text
        #Guardamos la busqueda realizada
        self.busqueda = busqueda
        #Llamamos al metodo que crea la carpeta
        self.checking_files()
        #Llamamos al metodo que grafica
        self.graph()
        #Guardamos la ruta de el directorio donde se guardaran las imagenes
        self.dir_name = f'Images_{self.busqueda.replace(" ","")}/'


    #Metodo que crea la carpeta donde se guardaran las imagenes
    def checking_files(self):
        archivos = os.listdir()
        if f'Images_{self.busqueda.replace(" ","")}' not in archivos: 
            os.mkdir(f'Images_{self.busqueda.replace(" ","")}')

    #Metodo que retorna la ruta de la carpeta donde se guardaran las imagenes
    def graph(self):
        to_show = '$'+self.text+'$' #self.text.replace(" ","")
        #Limpia la ventana de la grafica
        plt.clf()
        #colocamos el titulo de la grafica
        plt.title(f"Busqueda: {self.busqueda}")
        #iniciamos una sentencia try-except para que no de error si no se puede graficar
        try:
            #Establecemos el tamaño de la letra en la grafica dependiendo del tamaño de la ecuacion
            if len(to_show) > 50:
                plt.text(0.5, 0.5, to_show, usetex=True, fontsize=12, ha="center")
            elif len(to_show) > 20 and len(to_show) < 50:
                plt.text(0.5, 0.5, to_show, usetex=True, fontsize=20, ha="center")
            else:
                plt.text(0.5, 0.5, to_show, usetex=True, fontsize=40, ha="center")
            #Eliminamos el eje x y y
            plt.xticks([])
            plt.yticks([])
            #Guardamos la imagen en la carpeta
            archivos = os.listdir(f'Images_{self.busqueda.replace(" ","")}')
            #Si no hay imagenes en la carpeta, guarda la primera
            if self.text+'.png' not in archivos:
                plt.savefig(f'Images_{self.busqueda.replace(" ","")}/'+self.text+'.png',dpi=100)
        #Si ocurre un error, no hace nada
        except Exception:
            print(f'Error en formula: {self.text}')
            pass