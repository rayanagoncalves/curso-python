# Exercício 1
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.available = True

    def __str__(self):
        return f'{self.title.ljust(20)} | {self.author.ljust(20)} | {self.publication_year}'
    
    def lend(self):
        if self.available:
            print('Livro está disponível')
            self.available = not self.available
        else:
            print('Livro não está disponível')

    @staticmethod
    def check_availabilty(year):
        availabilty_books = [book for book in Book.books if book.publication_year == year and book.available]
        return availabilty_books
