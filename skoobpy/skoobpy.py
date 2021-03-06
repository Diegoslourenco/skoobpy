import requests
import json
import csv

url_base = 'https://www.skoob.com.br'

def get_all_books(user_id):
    """
    Returns all the data books from a user
    """
    url = f'{url_base}/v1/bookcase/books/{user_id}'
    print(f'request to {url}')

    user = requests.get(url)
    total = user.json().get('paging').get('total')
    total_books = f'{url}/shelf_id:0/page:1/limit:{total}'

    books_json = requests.get(total_books).json().get('response')

    return books_json

def filter_desired(books_json):
    """
    Returns desired books from a JSON file
    """
    books = []

    for book in books_json:
        if book['desejado'] == 1:
            ed = book['edicao']

            # if there is a subtitle, it must be concatenate to title
            if ed['subtitulo'] != '':
                book_title = str(ed['titulo']) + ' - '+ str(ed['subtitulo'])
            else:
                book_title = ed['titulo']

            book_url = url_base + ed['url']
            book_data = [book_title, ed['autor'], ed['ano'], ed['paginas'], ed['editora'], book_url]
            books.append(book_data)
        
    return books

def filter_readed(books_json):
    """
    Returns readed books from a JSON file
    """
    books = []

    for book in books_json:
        if book['tipo'] == 1:
            ed = book['edicao']

            # if there is a subtitle, it must be concatenate to title
            if ed['subtitulo'] != '':
                book_title = str(ed['titulo']) + ' - '+ str(ed['subtitulo'])
            else:
                book_title = ed['titulo']

            book_url = url_base + ed['url']
            book_data = [book_title, ed['autor'], ed['ano'], ed['paginas'], ed['editora'], book_url]
            books.append(book_data)
        
    return books

def filter_currently_reading(books_json):
    """
    Returns currently reading books from a JSON file
    """
    books = []

    for book in books_json:
        if book['tipo'] == 2:
            ed = book['edicao']

            # if there is a subtitle, it must be concatenate to title
            if ed['subtitulo'] != '':
                book_title = str(ed['titulo']) + ' - '+ str(ed['subtitulo'])
            else:
                book_title = ed['titulo']

            book_url = url_base + ed['url']
            book_data = [book_title, ed['autor'], ed['ano'], ed['paginas'], ed['editora'], book_url]
            books.append(book_data)
        
    return books


def export_csv(books_list, file_name):
    """
    Exports the data to a CSV file
    """

    header = ['Title', 'Author', 'Published Year', 'Pages', 'Publisher', 'Skoob\'s Page']

    with open(f'{user_id}.csv', 'w', encoding='utf-8', newline='') as csvfile:
        data = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        data.writerow(header)

        for book in books_list:
            data.writerow(book)
    
    return

    



    