def validBookObject(bookObject):
    if ("name" in bookObject
        and "price" in bookObject
            and "isbn" in bookObject):
        return True
    else:
        return False

valid_object = {
        'name': 'Test',
        'price': 1.99,
        'isbn': 1234567890
}

missing_name = {
        'price': 1.99,
        'isbn': 1234567890
}

missing_isbn = {
        'name': 'Test',
        'price': 1.99,
}

missing_price = {
        'name': 'Test',
        'isbn': 1234567890
}
