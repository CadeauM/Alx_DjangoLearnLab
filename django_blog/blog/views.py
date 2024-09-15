from django.shortcuts import render 
from django.shortcuts import redirect
from django.contrib import messages
from .forms import UserRegisterForm  # Importing the forms file
from django.contrib.auth.decorators import login_required  # Ensures only logged-in users can access the profile page
from django.shortcuts import get_object_or_404 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
# This will handle the view that handles user registration
def register(request):
    if request.method == 'POST':  # the user submits the form
        form = UserRegisterForm(request.POST)  # Fill the form with submitted data
        if form.is_valid():  # check if form is valid then save it. 
            form.save() 
            messages.success(request, 'Your account has been created, you can log in.')  # success message!
            return redirect('login')  # redirects to login page.
        else:
            form = UserRegisterForm()  # user just checking page.
            return render(request, 'blog/register.html', {'form': form})

@login_required  # this is a decorator.
def profile(request):
    return render(request, 'blog/profile.html')  # This shows the profile page

# this view helps to display all the posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # html template to display here
    context_object_name = 'posts'
    ordering = ['-date_posted']  # this displays the newly posts first(date).

# the detailview displys a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# the createview allows the users to  create and add new posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']  # These are the fields that will appear in the form
    template_name = 'blog/post_form.html' 
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# the updateview allows users to edit their posts.
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    
    def test_func(self):  # the logged-in user has to be the author
        post = self.get_object()
        return self.request.user == post.author

# the deleteview allows users to delete their own posts.
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    success_url = reverse_lazy('post-list')  # Redirects to the post list after deleting.
    template_name = 'blog/post_confirm_delete.html'
    
    def test_func(self):
        post = self.get_object() 
        return self.request.user == post.author

