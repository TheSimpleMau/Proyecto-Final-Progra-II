#######################################
###Importando los modulos necesarios###
#######################################
#Para hacer las peticiones HTTP
import requests
#Para leer el contenido de un archivo HTML
import lxml.html as html
#Para poder crear archivo y poder manejarlos
import os
#Para descartar los caracteres especiales
from string import ascii_letters, digits, punctuation
#Para hacer la busqueda de la informacion
from googlesearch import search


#######################################
###Clase para obtener la informacion###
#######################################

class GetFormulas:
    #Al constructor se le pasa la formula que se quiere buscar
    def __init__(self,to_search:str)->None:
        #Se guarda la formula que se quiere buscar
        self.to_search = to_search
        #Se obtienen los links de la formula
        self.getting_links = self.get_links()
        #Se guarda la informacion de la formula
        self.math_formulas = self.get_info()
        #Se crea una archivo para guardar la informacion
        self.file_with_formulas()


    #Metodo para obtener los links de la formula
    def get_links(self)->list:
        #Creando una lista para guardar los links
        links = []
        #Se busca la formula en google con la funcion search
        #Esta función lo que hara es buscar la formula en google y obtener los links de Wikipedia en español
        #Obtendrá unicamente los primeros 10 links
        for link in search(self.to_search+' wikipedia en español', tld='co.in', num=10, stop=10, pause=2):
            links.append(link)
        return links
    
    def get_info(self)->list:
        #Se crea una lista para guardar la informacion final
        final_formulas = []
        #Se crea un ciclo for para recorrer los links
        for link in self.getting_links:
            #Se hace la peticion a la pagina
            response = requests.get(link)
            #Se verifica que la peticion se haya realizado correctamente
            #Esto quiere decir que la pagina exista y no haya sido bloqueada por alguna restricción
            if response.status_code == 200:
                #Creamos una sentencia try-except para evitar que el programa se cierre al encontrar un error
                try:
                    #Se obtiene el contenido de la pagina
                    parsed = html.fromstring(response.content.decode('utf-8'))
                    #Ahora, obtendremos el contenido de la pagina, en este caso, las formulas.
                    #Hay que tener en cuenta que, lo que obtendremos realmente no son formulas,
                    #Sino que obtendremos todos los textos que sean de tipo mathml, por lo que hay que filtrarlo.
                    try:
                        #Se obtienen los textos de la pagina que sean de tipo mathml
                        cleaned_math_fomula = []
                        #Se crea una lista para guardar las formulas pero sin datos que nos interesen
                        maths_fomulas = parsed.xpath('//span[@class="mwe-math-mathml-inline mwe-math-mathml-a11y"]//./text()')
                        #Se recorre la lista de formulas
                        for formula in maths_fomulas:
                            #Se verifica que la formula tenga mas de 5 caracteres
                            #Esto quiere decir que no sea una formula vacia y/o muy corta.
                            if len(''.join(formula)) > 5:
                                #Se verifica que la formula no empiece con un salto de linea
                                if formula[0] != '\n':
                                    #Se remueve el displaystyle
                                    formula = formula.replace('\\displaystyle ','')
                                    #Se crea una lista para guardar los caracteres de la formula
                                    new_formula = [chars for chars in formula]
                                    #Se remueve el primer caracter si es un espacio en blanco o un espacio vacio
                                    if new_formula[0] == '' or new_formula[0] == ' ':
                                        new_formula.pop(0)
                                    #Se remueve el primer y ultimo caracter.
                                    #Esto pues, cuando obtenemos las formualas, estas siempre llevan al inicio
                                    #y al final unas llaves, las cuales no nos interesan
                                    itera = 0
                                    for _ in new_formula:
                                        if itera == 0 or itera == len(new_formula)-1:
                                            new_formula[itera] = ''
                                        itera += 1
                                    formula = ''.join(new_formula)
                                    #Por último, comprobamos que la formula no contenga caracteres especiales
                                    for char in formula:
                                        if char not in ascii_letters and char not in digits and char not in punctuation:
                                            break
                                    #Al final, despues de limpiar la formula, si sigue teniendo más de 5 caracteres
                                    #entonces, es una formula que nos interesa
                                    if len(''.join(formula)) > 5:
                                        cleaned_math_fomula.append(formula)
                        #Ahora que ya tenemos las formulas, se procede a obtener solo las primeras 10 formulas
                        if len(cleaned_math_fomula) > 10:
                            cleaned_math_fomula = cleaned_math_fomula[:10]
                        #Se retorna la lista de formulas
                        final_formulas = final_formulas + cleaned_math_fomula
                    except IndexError:
                        print('Error while execution. Index error')
                except UnicodeDecodeError:
                    print('Error while execution. Unicode error')
            #En caso de que no se haya podido realizar la peticion, se retorna un mensaje de error
            else:
                print(f'Cannot enter into the website\nError {response.status_code} on the website.')
        return final_formulas

    #Metodo para generar un archivo con la informacion de la formulas
    def file_with_formulas(self):
        #Primero, revisamos si es que ya existe un archivo con la informacion de las formulas
        os.system('ls -a > cheking_files.txt')
        #Se lee el archivo
        with open('cheking_files.txt','r') as file:
            #Se guarda la informacion en una lista
            lines = file.readlines()
            #Se busca el archivo con las formulas
            if f'.formulas para {self.to_search.lower()}.txt\n' not in lines:
                #Se crea el archivo
                with open(f'.formulas para {self.to_search.lower()}.txt','w') as new_file:
                    #Se escribe primero cual fue la busqueda
                    new_file.write(f'BUSQUEDA:{self.to_search}\n')
                    #Se escribe la informacion en el archivo
                    #Como cada 10 formulas se cambia de link, también se informa de a que link pertencen
                    i = 0
                    k = 0
                    for formula in self.math_formulas:
                        if i == 0 or i%10==0:
                            new_file.write(f'FORMULAS OBTENIDAS DE:{self.getting_links[k]}\n')
                            k += 1
                        new_file.write(f'{formula}\n')
                        i += 1
                    new_file.close()
            else:
                #Si ya existe el archivo, simplemente se lee la informacion
                print('El archivo ya existe')
            file.close()
        #Se elimina el archivo temporal
        os.system('rm cheking_files.txt')
