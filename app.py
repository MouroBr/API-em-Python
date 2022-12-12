from flask import Flask, make_response, jsonify, request
import bookRepository

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/book/<book_id>', methods=['GET'])
def getBook(book_id):
    book = bookRepository.getById(book_id)
    return make_response(jsonify(book.to_json()))


@app.route('/book', methods=['POST'])
def createBook():
    book = bookRepository.create(request.json['autor'],
                                 request.json['titulo'],
                                 request.json['anoPublicacao'],
                                 request.json['pais'])

    return make_response(jsonify(id=book.id), 201)


@app.route('/book/<book_id>', methods=['DELETE'])
def deleteBook(book_id):
    if bookRepository.removeById(book_id):
        return make_response([], 204)

    return make_response(jsonify([]), 404)


@app.route('/books', methods=['GET'])
def getBooks():
    allBooks = bookRepository.getAllBooks()

    responseBooks = []
    for book in allBooks:
        responseBooks.append(book.to_json())

    return make_response(jsonify(responseBooks))


app.run()
