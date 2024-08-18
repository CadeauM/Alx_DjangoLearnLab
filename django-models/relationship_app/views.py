from .models import Library
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import BookForm  # Assume you have a form for the Book model

from django.views.generic import DetailView   # DetailView is django built in view that displays details about a single object here which is Library 
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

from .models import Library
from django.views.generic.detail import DetailView # DetailView is django built in view that displays details about a single object here which is Library 
from django.contrib.auth import login
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.


def index(request):
    return HttpResponse("Hello, this is the index page.")

def home(request):
    return HttpResponse("<h1>Welcome to the Relationship App</h1>")

# FUNCTION-BASED VIEW

def list_books(request):  # the function takes the request and fetches all the books in the database
    books = Book.objects.all()  # instruction to fetch all the books in database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # this tells Django to pass the list_books.html and pass the list of books to it.

# CLASS-BASED VIEW

class LibraryDetailView(DetailView):  # The LibraryDetailView is a class-based view that shows detail about a specific library
    model = Library  # this tells Django that this view is for the library model
    template_name = 'relationship_app/library_detail.html'  # template_name is used to render the view
    context_object_name =  'library'  # specifies the name the template will use to access the library object

# LOGIN VIEW
class LoginView(auth_views.LoginView):
    template_name = 'relationship_app/login.html'

# LOGOUT VIEW
class LogoutView(auth_views.LogoutView):
    template_name = 'relationship_app/logout.html'

# REGISTRATION VIEW
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# HELPER FUNCTIONS TO CHECK THE USER ROLES
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# This is the admin view
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome Admin!")

# This is the Librarian View
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome Librarian!")

# This is the Member View
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome Member!")

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Adjust to your actual book list view name
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})

