from django.test import Client
from django.test import TestCase

from books.models import Book, Author


class TestBooks(TestCase):
    def setUp(self):
        self.client = Client()
        author = Author.objects.create(name='Ivanov I.I.')
        book = Book.objects.create(name='My first book', author=author)

    def test_main(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        resp = response.content.decode('utf-8')
        self.assertIn('Далекосибирск', resp)


    def test_book_list(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('object_list', response.context)


    def test_book_detail(self):
        response = self.client.get('/books/')
        self.assertEqual(len(response.context['object_list']), 1)


    def tearDown(self):
        author = Author.objects.get(name='Ivanov I.I.')
        author.delete()
