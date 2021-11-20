import matplotlib.pyplot as plt
import os

class Plots:

    def __init__(self,text,busqueda) -> None:
        self.text = text
        self.busqueda = busqueda
        self.checking_files()
        self.graph()


    def checking_files(self):
        archivos = os.listdir()
        if f'Images_{self.busqueda.replace(" ","")}' not in archivos: 
            os.mkdir(f'Images_{self.busqueda.replace(" ","")}')


    def graph(self):
        to_show = '$'+self.text+'$'
        #Limpia la ventana de la grafica
        plt.clf()
        plt.title("LaTeX plot")
        try:
            if len(to_show) > 25:
                plt.text(0.5, 0.5, to_show, usetex=True, fontsize=20, ha="center")
            else:
                plt.text(0.5, 0.5, to_show, usetex=True, fontsize=40, ha="center")
            plt.xticks([])
            plt.yticks([])
            archivos = os.listdir(f'Images_{self.busqueda.replace(" ","")}')
            if self.text+'.png' not in archivos:
                plt.savefig(f'Images_{self.busqueda.replace(" ","")}/'+self.text+'.png')
        except Exception:
            print(f'Error en formula: {self.text}')
            pass