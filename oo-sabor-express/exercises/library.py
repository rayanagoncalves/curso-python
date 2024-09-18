from exercises_3 import Book

book_1 = Book('É assim que acaba', 'Colleen Hoover', 2016)
book_2 = Book('É assim que começa', 'Colleen Hoover', 2022)

print(book_1)
print(book_2)

book_1.lend()

Book.books = [book_1, book_2]

print(Book.check_availabilty(2016))