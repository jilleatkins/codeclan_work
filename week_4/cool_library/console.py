import pdb
from models.author import Author
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author1 = Author("Charlotte", "Bronte")
author_repository.save(author1)

author2 = Author("Thomas", "Hardy")
author_repository.save(author2)

book1 = Book("Jane Ayre", "author_id", "Gothic", "1847")
book_repository.save(book1)

book2 = Book("Villette", "author_id", "Gothic", "1853")
book_repository.save(book2)

book3 = Book("Tess of The D'Urbervilles", "author_id", "Romance", "1891")
book_repository.save(book3)

book4 = Book("Jude the Obscure", "author_id", "Classic", "1895")
book_repository.save(book4)

