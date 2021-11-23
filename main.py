from tkinter import *
from Plots import *
from WebScraping import *
from Display import *

a_buscar = input('¿Qué formula/ecuacion quieres buscar? ')
resultado = GetFormulas(a_buscar)
for formula in resultado.math_formulas:
    Plots(formula,a_buscar)
os.system('python3 Display.py')