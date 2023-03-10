from users.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create adm"

    def add_arguments(self, parser):
        parser.add_argument(
            "--username",
            type=str,
            help="indicate the name of the adm to be created",
        )
        parser.add_argument(
            "--password",
            type=str,
            help="indicate the password of the adm to be created",
        )
        parser.add_argument(
            "--email",
            type=str,
            help="indicate the email to be created",
        )

    def handle(self, *args, **kwargs):
        user = kwargs["username"]
        password = kwargs["password"]

        email = kwargs["email"]

        User.objects.create_superuser(
            type_user="admin", username=user, password=password, email=email
        )
