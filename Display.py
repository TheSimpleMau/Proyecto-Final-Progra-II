from tkinter import*
import os

class Display:

    def __init__(self,path) -> None:
        self.path = path
        os.chdir(self.path)
        self.archivos = os.listdir()
        self.image_list=[]
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

        def forward(image_number):
            global button_forward
            global button_back
            my_label.config(image=self.image_list[image_number-1])
            button_forward = Button(self.ventana, text= ">>", command=lambda: forward(image_number+1))
            button_back = Button(self.ventana, text="<<",command=lambda: back(image_number-1) )
            if image_number == len(self.image_list):
                button_forward = Button(self.ventana, text=">>" , state=DISABLED )
            my_label.grid(row=0,column=0,columnspan=3)
            button_back.grid(row=1,column=0)
            button_forward.grid(row=1,column=2)

        def back(image_number):
            global button_forward
            global button_back
            my_label.config(image=self.image_list[image_number-1])
            button_forward = Button(self.ventana, text= ">>", command=lambda: forward(image_number+1))
            button_back = Button(self.ventana, text="<<",command=lambda: back(image_number-1) )
            if image_number == 1:
                button_back = Button(self.ventana,text="<<", state=DISABLED)
            my_label.grid(row=0,column=0,columnspan=3)
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