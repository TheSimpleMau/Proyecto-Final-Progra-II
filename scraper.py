import requests
import lxml.html as html
import os
import datetime
from googlesearch import search
from bs4 import BeautifulSoup


#has una funcion que busque algo en google y devuelva una lista de links

def busqueda(to_search):
    links = []
    for link in search(to_search+' wikipedia', tld="co.in", num=10, stop=10, pause=2):
        links.append(link)
    return links


def parse_content():
    pass


def parse_home():
    try:
        response = requests.get()
        if response.status_code == 200:
            print('Si jala')
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def main():
    links = busqueda('Ecuaciones de Maxwell')


if __name__ == '__main__':
    main()