from rest_framework.routers import DefaultRouter
from django.urls import path, include 
from .views import PostViewSet, CommentViewSet 
from django.urls import path
from .views import UserFeedView

router = DefaultRouter() 
router.register(r'posts', PostViewSet) 
router.register(r'comments', CommentViewSet) 

urlpatterns = [ 
    path('', include(router.urls)),
    path('feed/', UserFeedView.as_view(), name='user-feed'),
    
]

