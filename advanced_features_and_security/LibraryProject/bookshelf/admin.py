from django.contrib import admin
from .models import Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

@admin.register(Book)  #this registers the Book model with the django admin site
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # this will show the details of each book in the admin panel
    search_fields = ('title', 'author')  # you can then search the books in the panel by the title or author
    list_filter = ('publication_year',) # the filter to the sidebar so if you need you can search the books by their publication year

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