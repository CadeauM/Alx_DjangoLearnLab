from django.urls import path
from django.contrib.auth import views as auth_views  # we are importing the login/logout views
from . import views   # we are importing the views we have create for registration and profile.
from .views import PostListView
from .views import PostDetailView
from .views import PostCreateView
from .views import PostUpdateView
from .views import PostDeleteView
# Defining the paths for login, logout, registration, and profile

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'), 
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/update/', PostByTagListView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:post_id>/comments/new/', views.add_comment, name='add_comment'),  # This URL is for adding a new comment to a post.
    path('comment/<int:pk>/update/', views.update_comment, name='update_comment'), 
    path('post/<int:pk>/comments/new/', views.add_comment, name='add_comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('search/', views.search_posts, name='search_posts'),   # URL for searching posts
    path('tags/<slug:tag_slug>/', views.posts_by_tag, name='posts_by_tag'),  # URL for viewing posts by tag

]
