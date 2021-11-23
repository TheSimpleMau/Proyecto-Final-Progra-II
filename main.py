#######################################
###Importando los modulos necesarios###
#######################################
#Importamos la clase Plots que crea los textos en Latex
from Plots import *
#Importamos la clase WebScraping que realiza el scraping de la pagina
from WebScraping import *

########################
###Programa principal###
########################
#Le preguntamos al usuario que formula/ecuacion quiere buscar
a_buscar = input('¿Qué formula/ecuacion quieres buscar? ')
#Obtenemos las formulas de wikipedia
scrap = GetFormulas(a_buscar)
#Para cada formula, generamos un png que será la ecuacion en latex
for formula in scrap.math_formulas:
    Plots(formula,a_buscar)
#Por último, como existe un error entre los modulos de tkinter y matplotlib,
#ejecutamos desde la terminal el archivo Display que nos muestra los png
#generados.
os.system('python3 Display.py')