from unittest import TestCase
from store.serializers import BooksSerializer
from store.models import Book

class BookSerializersTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Test book 1', price=25, author_name='Author 1')
        book_2 = Book.objects.create(name='Test book 2', price=55, author_name='Author 2')
        data = BooksSerializer([book_1, book_2], many=True).data 
        excepted_data = [
            {
                'id': book_1.id,
                'name': 'Test book 1',
                'price':'25.00',
                'author_name': 'Author 1'
            },
            {
                'id': book_2.id,
                'name': 'Test book 2',
                'price': '55.00',
                'author_name': 'Author 2'
            }
        ]
        print('TESTING DATA FROM models.py: \n ========== \n',data, '\n')
        self.assertEqual(excepted_data, data)