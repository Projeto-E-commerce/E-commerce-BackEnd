from users.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = "Create adm"

    def add_arguments(self, parser):
        parser.add_argument(
            "username",
            type=str,
            help="indicate the name of the adm to be created",
        )
        parser.add_argument(
            "password",
            type=str,
            help="indicate the password of the adm to be created",
        )

    def handle(self, *args, **kwargs):
        user = kwargs["username"]
        password = kwargs["password"]
        User.objects.create_superuser(username="user", password="password")
