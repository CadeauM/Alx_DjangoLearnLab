from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def admin_check(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(admin_check)
def admin_view(request):
    return render(request, 'admin_view.html')
