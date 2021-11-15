import requests
import lxml.html as html
import os
import datetime
import cairosvg
import urllib.request
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
                if formula[0]=='{':
                    formula = formula.replace('{','')
                    formula = formula.replace('}','')
                    fromula = formula.replace('\\\\\\','*')
                    cleaned_math_fomula.append(formula)
                else:
                    pass
            if len(cleaned_math_fomula)>10:
                return cleaned_math_fomula[0:9]
            return cleaned_math_fomula
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
        else:
            print(f'Cannot enter into the website\nError {response.status_code}')
            return


def main():
    to_search = input('Que quieres buscar en wikipedia? ')
    links = getting_links(to_search)
    parse_home(links)


if __name__ == '__main__':
    main()