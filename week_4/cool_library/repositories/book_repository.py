from db.run_sql import run_sql
import repositories.author_repository as author_repository
from models.book import Book

def select_all():
  books = []

  sql = "SELECT * FROM books"
  results = run_sql(sql)

  for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row('id'), row('title'), author, row('genre'), row('year'))
        books.append(book)
  return books

def delete(id):
    sql = "DELETE  FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql, values)