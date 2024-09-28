from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer

# Create your views here.
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self): 
        return self.request.user.notifications.all().order_by('-timestamp')

@login_required
def notifications(request):
    notifications = Notification.objects.filter(recipient=request.user, read=False).order_by('-timestamp')
    return JsonResponse({'notifications': list(notifications.values())})
