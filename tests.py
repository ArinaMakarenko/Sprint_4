import pytest
from main import BooksCollector


class TestBooksCollector:

    # Проверка добавления двух книг в словарь books_genre
    def test_add_new_book_add_two_books(self, collection):
        books = ['Гарри Поттер', 'Властелин колец']
        for book in books:
            collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 2

    # Проверка с шагом вне граничных значений метода add_new_book(0 символов и больше 40)
    @pytest.mark.parametrize('book',
                             ['', 'ГарриПоттерГарриПоттерГарриПоттерГарриПоттер']
                             )
    def test_add_new_book_add_incorrect_name_failed(self, book, collection):
        collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 0

    # Проверка установления жанра по умолчанию
    def test_add_new_book_check_genre_success(self, collection):
        first_book = 'Гарри Поттер'
        collection.add_new_book(first_book)
        assert collection.get_book_genre(first_book) == ''

    # Проверка повторного добавления одной книги
    def test_add_new_book_add_double_books_failed(self, collection):
        books = ['Гарри Поттер', 'Гарри Поттер']
        for book in books:
            collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 1

    # Проверка добавления жанра
    def test_set_book_genre_added(self, collection):
        first_book = 'Укрытие'
        genre = 'Фантастика'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, genre)
        assert collection.get_book_genre(first_book) == genre

    # Проверка изменения жанра
    def test_set_book_genre_changed(self, collection):
        first_book = 'Укрытие'
        genre = 'Фантастика'
        other_genre = 'Детективы'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, genre)
        collection.set_book_genre(first_book, other_genre)
        assert collection.get_book_genre(first_book) == other_genre

    # Проверка добавления жанра не из списка
    def test_set_book_genre_missing_genre_not_added(self, collection):
        first_book = 'Укрытие'
        missing_genre = 'Приключения'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, missing_genre)
        assert collection.get_book_genre(first_book) == ''

    # Проверка вывода книги определенного жанра
    def test_get_books_with_specific_genre_success(self, collection_five_books):
        assert collection_five_books.get_books_with_specific_genre('Ужасы') == ['Пила']

    # Проверка вывода отсутствующей книги определенного жанра
    def test_get_books_with_specific_genre_missing_book(self, collection_five_books):
        assert len(collection_five_books.get_books_with_specific_genre('Драма')) == 0

    # Проверка вывода списка книг с жанром для детей
    def test_get_books_for_children_success(self, collection_five_books):
        children_books = collection_five_books.get_books_for_children()
        assert len(children_books) == 3 and children_books == ['Укрытие', 'Золушка', 'Ирония судьбы']

    # Проверка добавления книги в избранное
    def test_add_book_in_favorites_add_one_book_added(self, collection):
        first_book = 'Хоббит'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        favorites = collection.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book

    # Проверка добавления книги не из списка в избранное
    def test_add_book_in_favorites_add_missing_book_not_added(self, collection):
        first_book = 'Гарри Поттер'
        collection.add_book_in_favorites(first_book)
        assert len(collection.get_list_of_favorites_books()) == 0

    # Проверка повторного добавления книги в избранное
    def test_add_book_in_favorites_add_double_books_not_added(self, collection):
        first_book = 'Гарри Поттер'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.add_book_in_favorites(first_book)
        favorites = collection.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book

    # Проверка удаления книги из списка избранное
    def test_delete_book_from_favorites_book_deleted(self, collection):
        first_book = 'Гарри Поттер'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.delete_book_from_favorites(first_book)
        assert len(collection.get_list_of_favorites_books()) == 0
