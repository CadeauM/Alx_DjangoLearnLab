from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Library
from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .forms import ExampleForm

# Create your views here.

def LibraryDetailView(request, pk):
    library = get_object_or_404(Library, pk=pk)
    return render(request, 'library_detail.html', {'library': library})

from django.shortcuts import render

def list_books(request):
    # Your view logic here
    pass

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            # redirect to some page
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the book list or another page
    return render(request, 'delete_book_confirm.html', {'book': book})

def index(request):
    return render(request, 'index.html')



@login_required
def index(request):
    # Your view logic here
    return render(request, 'index.html')

@permission_required('bookshelf.view_book', raise_exception=True)
def book_detail(request, book_id):
    # Your view logic here
    return render(request, 'book_detail.html')

@method_decorator(login_required, name='dispatch')
class IndexView(View):
    def get(self, request):
        # Your view logic here
        return render(request, 'index.html')

@method_decorator(permission_required('bookshelf.view_book', raise_exception=True), name='dispatch')
class BookDetailView(View):
    def get(self, request, book_id):
        # Your view logic here
        return render(request, 'book_detail.html')

from .decorators import custom_permission_required

@custom_permission_required
def some_view(request):
    # Your view logic here
    return render(request, 'some_template.html')

def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books})
