# qa_python
Для класса BooksCollector реализованы следующие тесты:

* Проверка добавления двух книг в словарь books_genre: test_add_new_book_add_two_books
* Проверка с шагом вне граничных значений метода add_new_book (0 символов и больше 40): test_add_new_book_add_incorrect_name_failed
* Проверка установления жанра по умолчанию: test_add_new_book_check_genre_success
* Проверка повторного добавления одной книги: test_add_new_book_add_double_books_failed
* Проверка добавления жанра: test_set_book_genre_added
* Проверка изменения жанра: test_set_book_genre_changed
* Проверка добавления жанра не из списка: test_set_book_genre_missing_genre_not_added
* Проверка вывода книги определенного жанра: test_get_books_with_specific_genre_success
* Проверка вывода отсутствующей книги определенного жанра: test_get_books_with_specific_genre_missing_book
* Проверка вывода списка книг с жанром для детей: test_get_books_for_children_success
* Проверка добавления книги в избранное: test_add_book_in_favorites_add_one_book_added
* Проверка добавления книги не из списка в избранное: test_add_book_in_favorites_add_missing_book_not_added
* Проверка повторного добавления книги в избранное: test_add_book_in_favorites_add_double_books_not_added
* Проверка удаления книги из списка избранное: test_delete_book_from_favorites_book_deleted

Запуск тестов
pytest -v

Оценка покрытия
pytest --cov=main

Подробная оценка покрытия с учетом ветвления
pytest --cov=main --cov-branch --cov-report=html