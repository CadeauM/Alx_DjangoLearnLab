from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2'),
        }),
    )
    
    # Define the fields to be displayed in the User admin list view.
    list_display = ('username', 'email', 'date_of_birth', 'profile_photo', 'is_staff', 'is_active')
    
    # Define the fields to be used in searching Users.
    search_fields = ('username', 'email')
    
    # Define the fields to be used in filtering Users.
    ordering = ('-date_joined',)
admin.site.register(CustomUser, CustomUserAdmin)
