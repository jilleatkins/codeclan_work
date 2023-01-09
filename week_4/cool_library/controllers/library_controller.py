from flask import render_template, Blueprint, request, redirect
from repositories import book_repository, author_repository
from models.book import Book
import pdb

book_blueprint = Blueprint("books", __name__)

@book_blueprint.route('/books')
def books():
    all_books_list = book_repository.select_all()
    return render_template('/books/index.html'), all_books_key=all_books_list
