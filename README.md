# 📘🐍 Skoobpy 

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Gives you methods to extract the users' data from [Skoob](https://www.skoob.com.br/).

## ⚙️ Installation

You can install Skoobpy from [PyPI](https://pypi.org/project/skoobpy/):

```bash
pip install skoobpy
```

## 💻 How to Use

You can run it as a module in a command line as `skoobpy` followed by an `user_id`. It is going to generate a csv file named `books_user_id.csv` with all informations of user's desired books.

    $ python skoobpy <user_id>



Alternatively, it is possible to import it.

```python
import skoobpy
from skoobpy import *
```

The functions are:

* `get_all_books(user_id)` receives a user id and returns all the books in the bookshelves as a JSON object.
*  The filter functions receive a JSON with a group of books and filter it according to the criteria in a list that contains the book title, author's name, book release year, number of pages, publisher, and the book URL in the skoob site.
    * `filter_desired(books_json)` returns the desired books.
    * `filter_readed(books_json)` returns the readed books.
    * `filter_currently_reading(books_json)` returns currently reading books.
* `export_csv(books_list, file_name)` exports a CSV file named as a given file name that contains the data in a list of books provided.



## 📑 Release History

* 0.1.0
    * First version - extract users' desired books in CSV file



## ⚖️ License

Distributed under the MIT license. See [`LICENSE`](https://github.com/Diegoslourenco/skoopy/blob/main/LICENSE) for more information.



## 🚧🚀 Contributing


Feel free to contribute with anything.

[In case of any doubt, see this.](https://github.com/firstcontributions/first-contributions)

To start with development, don't forget to install:

```python
$ pip install -r requirements.txt
```
