#######################################
###Importando los modulos necesarios###
#######################################
#Del modulo tkinter importamos todo
from tkinter import *
#Importamos os
import os

##############################
###Creando la clase Display###
##############################

class Display:

    ##Constructor de la clase
    #Lo único que le pediremos es la ruta a los png generados con Plots.py
    def __init__(self,path) -> None:
        #Guradamos la ruta
        self.path = path
        #Nos cambiamos de directorio
        os.chdir(self.path)
        #Obtenemos la lista de los png
        self.archivos = os.listdir()
        #Creamos una lista de los png
        self.image_list=[]
        #Creamos una lista con las ecuaciones de Latex
        self.latex_equations = []
        #Creamos una nueva ventana para mostrar las imagenes
        self.window = Tk()
        #Configuramos el color de fondo
        self.window.configure(background='#0e108f')
        #Nombre de la ventana
        self.window.title("Plot de LaTeX")
        #Configuramos el pading de la ventana
        self.window.configure(padx=50,pady=50)
        #Creamos un contador para saber en que imagen estamos
        i=0
        #Recorremos la lista de los archivos
        for imagen in self.archivos:
            #Si el archivo es un png
            if imagen.endswith(".png"):
                #Agregamos la ecuacion a la lista de ecuaciones
                self.latex_equations.append(imagen.replace(".png",""))
                #Cambiamos el nombre del archivo
                re_name = "img"+str(i)+".png"
                os.rename(imagen,re_name)
                #Agregamos la imagen a la lista de imagenes
                self.image_list.append(PhotoImage(master=self.window,file=re_name))
                #Aumentamos el contador
                i+=1
        #Creamos una etiqueta que va a contener la imagen
        my_label = Label(image=self.image_list[0],bg='#0e108f',highlightthickness=0)
        my_label.grid(row=0,column=0,columnspan=3)
        #Creamos una etiqueta que va a contener la ecuacion
        latex_label = Label(text='Ecuacion en LaTeX:',bg='#0e108f',highlightthickness=0)
        latex_label.grid(row=2,column=0)
        latex_text = Text(self.window,height=1,highlightthickness=0)
        latex_text.grid(row=2,column=1,columnspan=2)
        latex_text.insert(END,self.latex_equations[0])

        #Metodo que se ejecuta al presionar el boton de adelante
        def forward(image_number):
            global button_forward
            global button_back
            my_label.config(image=self.image_list[image_number-1])
            latex_text.delete(1.0,END)
            latex_text.insert(END,self.latex_equations[image_number-1])
            latex_label = Label(text='Ecuacion en LaTeX:',bg='#0e108f')
            latex_label.grid(row=2,column=0)
            button_forward = Button(self.window, text= ">>", command=lambda: forward(image_number+1),highlightthickness=0,bg='#0e108f')
            button_back = Button(self.window, text="<<",command=lambda: back(image_number-1),highlightthickness=0,bg='#0e108f')
            if image_number == len(self.image_list):
                button_forward = Button(self.window, text=">>" , state=DISABLED,highlightthickness=0,bg='#0e108f')
            my_label.grid(row=0,column=0,columnspan=3)
            latex_text.grid(row=2,column=1,columnspan=2)
            button_back.grid(row=1,column=0)
            button_forward.grid(row=1,column=2)

        #Metodo que se ejecuta al presionar el boton de atras
        def back(image_number):
            global button_forward
            global button_back
            my_label.config(image=self.image_list[image_number-1])
            latex_text.delete(1.0,END)
            latex_text.insert(END,self.latex_equations[image_number-1])
            latex_label = Label(text='Ecuacion en LaTeX:',bg='#0e108f')
            latex_label.grid(row=2,column=0)
            button_forward = Button(self.window, text= ">>", command=lambda: forward(image_number+1),highlightthickness=0,bg='#0e108f')
            button_back = Button(self.window, text="<<",command=lambda: back(image_number-1),highlightthickness=0,bg='#0e108f')
            if image_number == 1:
                button_back = Button(self.window,text="<<", state=DISABLED,highlightthickness=0,bg='#0e108f')
            my_label.grid(row=0,column=0,columnspan=3)
            latex_text.grid(row=2,column=1,columnspan=2)
            button_back.grid(row=1,column=0)
            button_forward.grid(row=1,column=2)
        
        #Creamos un boton para ir atras
        button_back = Button(self.window,text="<<", command=lambda: back(), state=DISABLED,highlightthickness=0,bg='#0e108f')
        #Creamos un boton para ir adelante
        button_forward = Button(self.window,text=">>", command= lambda: forward(2),highlightthickness=0,bg='#0e108f')
        #Creamos un boton para cerrar la ventana
        button_exit = Button(self.window,text="EXIT PROGRAM", command=self.window.quit,highlightthickness=0,bg='#0e108f')
        button_back.grid(row=1,column=0)
        button_exit.grid(row=1, column=1)
        button_forward.grid(row=1,column=2)

        self.window.mainloop()


#Creamos nuestro entry point
if __name__ == '__main__':
    #limpiamos la pantalla
    os.system("clear")
    #Buscamos la carpeta con los archivos
    os.system('ls -t > finding_files.txt')
    with open('finding_files.txt','r') as file:
        line = file.readlines()[1]
        line = line.replace('\n','/')
        file.close()
    #Removemos el archivo temporal
    os.system('rm finding_files.txt')
    #Creamos un objeto de la clase
    Display(line)