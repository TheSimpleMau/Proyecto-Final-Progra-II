import requests
import lxml.html as html
import os
# import datetime
# import cairosvg
# import urllib.request
from string import ascii_letters, digits, punctuation
from googlesearch import search


def getting_info(link:str):
    response = requests.get(link)
    if response.status_code == 200:
        try:
            parsed = html.fromstring(response.content.decode('utf-8'))
        except UnicodeDecodeError:
            return 'Unicode error'
        try:
            maths_fomulas = parsed.xpath('//span[@class="mwe-math-mathml-inline mwe-math-mathml-a11y"]//./text()')
            # print(maths_fomulas)
            cleaned_math_fomula = []
            for formula in maths_fomulas:
                if len(''.join(formula)) > 5:
                    if formula[0] != '\n':
                        formula = formula.replace('\\displaystyle ','')
                        new_formula = [chars for chars in formula]
                        if new_formula[0] == '' or new_formula[0] == ' ':
                            new_formula.pop(0)
                        itera = 0
                        for char in new_formula:
                            if itera == 0 or itera == len(new_formula)-1:
                                new_formula[itera] = ''
                            itera += 1
                        formula = ''.join(new_formula)
                        for char in formula:
                            if char not in ascii_letters or char in digits or char in punctuation:
                                break
                        if len("".join(formula)) > 5:
                            cleaned_math_fomula.append(formula)
                # if '\\displaystyle' in formula:
                #     formula = formula.replace('\\displaystyle','')
            if len(cleaned_math_fomula)>10:
                cleaned_math_fomula = cleaned_math_fomula[0:10]
            ###REVISAR SI FUNCIONA CON DOBLE DIAGONAL INVERTDIDA CON MATPLOTLIB###
            os.system('ls -a > check_files.txt')
            with open('check_files.txt','r') as file:
                files = file.readlines()
                if '.just_a_forgetable_text.txt\n' not in files:
                    os.system('touch .just_a_forgetable_text.txt')
                    with open('.just_a_forgetable_text.txt','w') as file:
                        file.write(f'LINK:{link}\n')
                        file.close()
                file.close()
            os.system('rm check_files.txt')
            with open('.just_a_forgetable_text.txt','a') as file:
                for formula in cleaned_math_fomula:
                    file.write(formula+'\n')
            finlas_formulas = []
            # os.system('open .just_a_forgetable_text.txt')
            # input()
            with open('.just_a_forgetable_text.txt','r') as file:
                for line in file:
                    line = line.replace('\n','')
                    finlas_formulas.append(line)
            return finlas_formulas
            # return cleaned_math_fomula
            # fullname = ''
            # urllib.request.urlretrieve(image,fullname+'.svg')
            # cairosvg.svg2png(url=f"./{fullname}.svg", write_to=f"./images/{fullname}.png")
            # os.remove(f"./{fullname}.svg")
        except IndexError:
            return


def getting_links(to_search):
    links = []
    for link in search(to_search+' wikipedia en español', tld="co.in", num=10, stop=10, pause=2):
        links.append(link)
    return links


def parse_home(links:list):
    for link in links:
        response = requests.get(link)
        if response.status_code == 200:
            print('Si jala')
            maths_formuls = getting_info(link)
            print(maths_formuls)
            # print(len(maths_formuls))
            # print(maths_formuls)
            # for text in maths_formuls:
            #     print(text)
        else:
            print(f'Cannot enter into the website\nError {response.status_code} on the website.')
            # return


def main():
    to_search = input('Que quieres buscar en wikipedia? ')
    links = getting_links(to_search)
    parse_home(links)
    os.system('cat .just_a_forgetable_text.txt')


if __name__ == '__main__':
    main()