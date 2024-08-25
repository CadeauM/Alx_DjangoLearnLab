from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book  # Ensure this path is correct

class Command(BaseCommand):
    help = 'Setup groups and permissions'

    def handle(self, *args, **options):
        # Create Groups
        editors, created = Group.objects.get_or_create(name='Editors')
        viewers, created = Group.objects.get_or_create(name='Viewers')
        admins, created = Group.objects.get_or_create(name='Admins')

        # Define Permissions
        permissions = {
            'can_view': 'Can view book',
            'can_create': 'Can create book',
            'can_edit': 'Can edit book',
            'can_delete': 'Can delete book',
        }

        # Assign Permissions to Groups
        for perm_name, perm_description in permissions.items():
            permission = Permission.objects.get(codename=perm_name)
            if perm_name in ['can_edit', 'can_create']:
                editors.permissions.add(permission)
            if perm_name == 'can_view':
                viewers.permissions.add(permission)
            admins.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('Successfully setup permissions and groups'))