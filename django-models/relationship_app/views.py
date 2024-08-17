from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import DetailView   # DetailView is django built in view that displays details about a single object here which is Library 
# Create your views here.


def index(request):
    return HttpResponse("Hello, this is the index page.")

def home(request):
    return HttpResponse("<h1>Welcome to the Relationship App</h1>")

# FUNCTION-BASED VIEW

def list_books(request):  # the function takes the request and fetches all the books in the database
    books = Book.objects.all()  # instruction to fetch all the books in database
    return render(request, 'list_books.html', {'books': books})  # this tells Django to pass the list_books.html and pass the list of books to it.

# CLASS-BASED VIEW

class LibraryDetailView(DetailView):  # The LibraryDetailView is a class-based view that shows detail about a specific library
    model = Library  # this tells Django that this view is for the library model
    template_name = 'Library_detail.html'  # template_name is used to render the view
    context_object_name =  'library'  # specifies the name the template will use to access the library object
