class Book(object):
    """docstring for Book"""
    def __init__(self, title):
        self.title = title

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title
        return NotImplemented
