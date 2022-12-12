import uuid
from book import Book

BOOKS_MEMORY = []

def getById(id):
  for book in BOOKS_MEMORY:
    if book.id == id:
        return book


def create(autor, titulo, ano, pais):
  book = Book(uuid.uuid4(), autor, titulo, ano, pais)
  BOOKS_MEMORY.append(book)
  return book

def removeById(id):
  for book in BOOKS_MEMORY:
    if book.id == id:
      BOOKS_MEMORY.remove(book)
      return True
  
  return False

def getAllBooks():
  return BOOKS_MEMORY