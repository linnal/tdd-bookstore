import pytest
from bookstore.bookstore import BookStore
from bookstore.book import Book


@pytest.fixture(scope="module")
def bookstore():
    return BookStore()


class TestBookstore(object):

    @pytest.fixture(autouse=True)
    def clean(request, bookstore):
        bookstore.empty()

    def test_creation_of_empty_book_store(self, bookstore):
        list_of_books = bookstore.all()

        assert 0 == len(list_of_books)

    def test_insertion_of_a_book(self, bookstore):
        bookstore.add(Book('title'))
        list_of_books = bookstore.all()

        assert 1 == len(list_of_books)

    def test_search_book_by_title(self, bookstore):
        book = Book('title')
        bookstore.add(book)
        searched_book = bookstore.search('title')[0]

        assert book == searched_book

    def test_search_book_that_contain_title(self, bookstore):
        bookstore.add(Book('first title'))
        bookstore.add(Book('second title'))
        searched_books = bookstore.search('title')

        assert 2 == len(searched_books)
        assert 'first title' in [book.title for book in searched_books]
        assert 'second title' in [book.title for book in searched_books]

    def test_remove_the_only_book_present(self, bookstore):
        bookstore.add(Book('title'))
        book = bookstore.remove(Book('title'))

        assert 0 == len(bookstore.all())
        assert 'title' == book.title

    def test_remove_book_in_head(self, bookstore):
        bookstore.add(Book('title one'))
        bookstore.add(Book('title two'))
        bookstore.add(Book('title three'))

        bookstore.remove(Book('title one'))

        assert 2 == len(bookstore.all())

    def test_remove_book_in_tail(self, bookstore):
        bookstore.add(Book('title one'))
        bookstore.add(Book('title two'))
        bookstore.add(Book('title three'))

        bookstore.remove(Book('title three'))

        assert 2 == len(bookstore.all())
        assert ['title one', 'title two'] == [b.title for b in bookstore.all()]
