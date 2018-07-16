from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'name': 'Green Eggs and Ham',
        'price': 7.99,
        'isbn': 978039400165
    },
    {
        'name': 'The Cat in the Hat',
        'price': 6.99,
        'isbn': 978039400193
    }
]

#POST /books
# {
#     'name': 'F',
#     'price': int,
#     'isbn': int
# }

def validBookObject(bookObject):
    if ("name" in bookObject
        and "price" in bookObject
            and "isbn" in bookObject):
        return True
    else:
        return False

#GET /books
@app.route('/books')
def hello_world():
    return jsonify({'books': books})

#POST /books
@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if (validBookObject(request_data)):
        books.insert(0, request_data)
        return "True"
    else:
        return "False"

#/int:isbn is a cast of the variable isbn to int
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book["isbn"] == isbn:
            return_value = {
                'name': book["name"],
                'price': book["price"]
            }
    return jsonify(return_value)


app.run(port=5000)
