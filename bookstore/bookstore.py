import pdb


class Node():
    def __init__(self, book):
        self.book = book
        self.next = None

    def has_next(self):
        return self.next is not None

    def is_empty(self):
        return self.book is None


class BookStore():
    """docstring for BookStore"""
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head

    def all(self):
        """Return a list of all Books."""
        return self._to_list()

    def add(self, book):
        if self._is_empty():
            self.head.book = book
        else:
            self.tail.next = Node(book)
            self.tail = self.tail.next

    def search(self, title):
        result = []
        current = self.head
        while current:
            if title in current.book.title:
                result.append(current.book)
            current = current.next
        return result

    def remove(self, book):
        if self.head.book == book:
            self.head = self.head.next
            return book

        current = self.head
        prev = current
        while current:
            if current.book == book:
                prev.next = current.next
                current.next = None
                return current.book
            prev = current
            current = current.next
        return None

    def empty(self):
        self.head = Node(None)
        self.tail = self.head

    def _to_list(self):
        result = []
        current = self.head
        while current is not None and current.book is not None:
            result.append(current.book)
            current = current.next
        return result

    def _is_empty(self):
        return self.head.book is None
