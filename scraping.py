import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#from flask import Flask, request
import pandas as pd

#code = 1380619

def getBooksByUserCode(code):

    books = []
    images = []

    #driver = webdriver.Chrome('./chromedriver')
    url = f"https://www.skoob.com.br/estante/livros/9/{code}/"
    data = requests.get(url)
    #driver.get(url)

    soup = BeautifulSoup(data.text, 'html.parser')

    for div in soup.find_all('div', attrs={'class':'drop-shadow-left ng-scope'}):
        name = div.find('img','tooltip')
        image = div.find('src')

        books.append(name.text)
        images.append(image[107:])

    df = pd.DataFrame({'Book Name':books, 'Book Image':images})
    df.to_csv('books.csv', index=False, encoding='utf=8')

    return
    
getBooksByUserCode(input("Enter the code: "))

