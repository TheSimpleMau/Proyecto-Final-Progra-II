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
        self.ventana = Tk()
        i=0
        for imagen in self.archivos:
            if imagen.endswith(".png"):
                self.latex_equations.append(imagen.replace(".png",""))
                re_name = "img"+str(i)+".png"
                os.rename(imagen,re_name)
                self.image_list.append(PhotoImage(master=self.ventana,file=re_name))
                i+=1
        my_label= Label(image=self.image_list[0])
        my_label.grid(row=0,column=0,columnspan=3)
        latex_label= Label(text='Ecuacion en LaTeX:')
        latex_label.grid(row=2,column=0)
        latex_text = Text(self.ventana,height=1)
        latex_text.grid(row=2,column=1,columnspan=2)
        latex_text.insert(END,self.latex_equations[0])

        def forward(image_number):
            global button_forward
            global button_back
            my_label.config(image=self.image_list[image_number-1])
            latex_text.delete(1.0,END)
            latex_text.insert(END,self.latex_equations[image_number-1])
            button_forward = Button(self.ventana, text= ">>", command=lambda: forward(image_number+1))
            button_back = Button(self.ventana, text="<<",command=lambda: back(image_number-1) )
            if image_number == len(self.image_list):
                button_forward = Button(self.ventana, text=">>" , state=DISABLED )
            my_label.grid(row=0,column=0,columnspan=3)
            latex_text.grid(row=2,column=0,columnspan=3)
            button_back.grid(row=1,column=0)
            button_forward.grid(row=1,column=2)

        def back(image_number):
            global button_forward
            global button_back
            my_label.config(image=self.image_list[image_number-1])
            latex_text.delete(1.0,END)
            latex_text.insert(END,self.latex_equations[image_number-1])
            button_forward = Button(self.ventana, text= ">>", command=lambda: forward(image_number+1))
            button_back = Button(self.ventana, text="<<",command=lambda: back(image_number-1) )
            if image_number == 1:
                button_back = Button(self.ventana,text="<<", state=DISABLED)
            my_label.grid(row=0,column=0,columnspan=3)
            latex_text.grid(row=2,column=0,columnspan=3)
            button_back.grid(row=1,column=0)
            button_forward.grid(row=1,column=2)
        

        button_back= Button(self.ventana,text="<<", command=lambda: back(), state=DISABLED)
        button_exit= Button(self.ventana,text="EXIT PROGRAM", command=self.ventana.quit)
        button_forward= Button(self.ventana,text=">>", command= lambda: forward(2))
        button_back.grid(row=1,column=0)
        button_exit.grid(row=1, column=1)
        button_forward.grid(row=1,column=2)

        self.ventana.mainloop()


if __name__ == '__main__':
    os.system("clear")
    os.system('ls -t > finding_files.txt')
    with open('finding_files.txt','r') as file:
        line = file.readlines()[1]
        line = line.replace('\n','/')
        file.close()
    os.system('rm finding_files.txt')
    Display(line)