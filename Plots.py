import matplotlib.pyplot as plt
import os

class Plots:

    def __init__(self,text,busqueda) -> None:
        self.text = text
        self.busqueda = busqueda
        self.checking_files()
        self.graph()
        self.dir_name = f'Images_{self.busqueda.replace(" ","")}/'


    def checking_files(self):
        archivos = os.listdir()
        if f'Images_{self.busqueda.replace(" ","")}' not in archivos: 
            os.mkdir(f'Images_{self.busqueda.replace(" ","")}')


    def graph(self):
        to_show = '$'+self.text+'$' #self.text.replace(" ","")
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
                try:
                    plt.savefig(f'Images_{self.busqueda.replace(" ","")}/'+self.text.replace(" ","")+'.png',dpi=100)
                except Exception:
                    plt.savefig(f'Images_{self.busqueda.replace(" ","")}\\'+self.text.replace(" ","")+'.png',dpi=100)
                else:
                    raise Exception
        except Exception:
            print(f'Error en formula: {self.text}')
            pass