import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("name", [
        "",
        "Тестовое название книги, которое превышает 40 символов"
    ])
    def test_add_new_book_invalid_name_not_added(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_set_book_genre_valid(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.books_genre('Дюна') == 'Фантастика'

    def test_get_books_genre_returns_dict(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_genre() == {'Дюна': 'Фантастика'}

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна']

    def test_add_new_book_without_genre(self, collector):
        collector.add_new_book('Дюна')
        assert collector.get_book_genre('Дюна') == ''

    def test_get_books_for_children_excludes_age_rated_genres(self, collector):
        collector.add_new_book("Страшная книга")
        collector.add_new_book("Детективная история")
        collector.set_book_genre("Страшная книга", "Ужасы")
        collector.set_book_genre("Детективная история", "Детективы")
        books_for_children = collector.get_books_for_children()
        assert "Страшная книга" and "Детективная история" not in books_for_children

    def test_books_collector_add_book_in_favorites(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert 'Дюна' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_existing_book_removes_successfully(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == []