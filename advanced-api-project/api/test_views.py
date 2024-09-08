from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author

class BookTests(APITestCase):
    def setUp(self):
        # Create an Author object to associate with Books
        self.author = Author.objects.create(name="Author One")

        # Create initial Book data for testing
        self.book_data = {'title': 'Test Book', 'publication_year': 2023, 'author': self.author.id}
        
        # URL for creating and getting books
        self.create_url = reverse('book-list')
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})

    def test_create_book(self):
        """Test that a Book can be created"""
        response = self.client.post(self.create_url, self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test Book')

    def test_get_book_list(self):
        """Test that the list of books can be retrieved"""
        Book.objects.create(title='Test Book', publication_year=2023, author=self.author)
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_book(self):
        """Test that a Book can be updated"""
        book = Book.objects.create(title='Old Title', publication_year=2022, author=self.author)
        update_data = {'title': 'Updated Title', 'publication_year': 2022, 'author': self.author.id}
        response = self.client.put(self.detail_url(book.id), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get().title, 'Updated Title')

    def test_delete_book(self):
        """Test that a Book can be deleted"""
        book = Book.objects.create(title='Test Book', publication_year=2023, author=self.author)
        response = self.client.delete(self.detail_url(book.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
class BookFilterSearchOrderTests(APITestCase):
    def setUp(self):
        # Create an Author object
        self.author = Author.objects.create(name="Author One")

        # Create Book objects
        self.book1 = Book.objects.create(title="Book One", publication_year=2021, author=self.author)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2022, author=self.author)
        self.book3 = Book.objects.create(title="Another Book", publication_year=2023, author=self.author)
        
        self.url = reverse('book-list')

    def test_filter_books_by_title(self):
        """Test filtering books by title"""
        response = self.client.get(self.url, {'title': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_search_books_by_title(self):
        """Test searching books by title"""
        response = self.client.get(self.url, {'search': 'Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should return 'Book One' and 'Book Two'

    def test_order_books_by_publication_year(self):
        """Test ordering books by publication_year"""
        response = self.client.get(self.url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book One')  # Oldest book first
        self.assertEqual(response.data[2]['title'], 'Another Book')  # Latest book last

