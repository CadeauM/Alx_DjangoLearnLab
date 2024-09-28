from django.shortcuts import render
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters
from rest_framework import generics, permissions
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification
from django.shortcuts import get_object_or_404
from django.shortcuts import generics.get_object_or_404(Post, pk=pk)
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):  
        # Get the users that the current user is following
        following_users = self.request.user.following.all() 
        # Return posts from followed users, ordered by creation date 
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user

        if Like.objects.filter(post=post, user=user).exists(): 
            return Response({'message': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
        Like.objects.create(post=post, user=user)
        
        # Create a notification for the post's author
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked your post',
            target=post
        ) 
        return Response({'message': 'Post liked successfully.'}, status=status.HTTP_200_OK)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user

        try:
            like = Like.objects.get(post=post, user=user)
            like.delete()
        except Like.DoesNotExist:
            return Response({'message': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Post unliked successfully.'}, status=status.HTTP_200_OK)

class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the users that the current user is following
        followed_users = self.request.user.following.all()
        # Return posts from followed users, ordered by creation date
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')
        
@login_required 
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if created:
        
        # Notify the post's author 
        Notification.objects.create(
            recipient=post.author, 
            actor=request.user, 
            verb='liked', 
            target=post 
        ) 
        return JsonResponse({'status': 'liked'})

@login_required
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    Like.objects.filter(user=request.user, post=post).delete()
    return JsonResponse({'status': 'unliked'})

