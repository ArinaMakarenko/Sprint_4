import pytest
from main import BooksCollector


@pytest.fixture
def collection():
    collection = BooksCollector()
    return collection

def pytest_make_parametrize_id(val):
    return repr(val)

@pytest.fixture
def collection_five_books(collection):
    collect = collection
    books = ['Укрытие',   'Пила', 'Шерлок Холмс', 'Золушка', 'Ирония судьбы']
    genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии' ]
    for i in range(5):
        collect.add_new_book(books[i])

    for i in range(5):
        collect.set_book_genre(books[i], genre[i])

    return collect