# utilisateurs/management/commands/create_profiles.py
from django.core.management.base import BaseCommand
from utilisateurs.models import Profil
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create profiles for all users'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            if not hasattr(user, 'profil'):
                Profil.objects.create(user=user)
                self.stdout.write(self.style.SUCCESS(f'Profile created for user {user.username}'))
            else:
                self.stdout.write(self.style.WARNING(f'Profile already exists for user {user.username}'))
