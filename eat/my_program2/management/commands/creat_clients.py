from django.core.management.base import BaseCommand
from my_program2.models import Client
from .my_generate import generate_name, generate_adres, generate_phone_number

class Command(BaseCommand):
    help = "Create Client"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count new Client')
        help = "Generate fake client, product, order"


    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            new_name = generate_name()
            new_telefon = generate_phone_number()
            new_adres = generate_adres()
            cliens = Client(name=f'Name{new_name}', email=f'{new_name}@mail.ru', telefon=new_telefon,
                            adres=new_adres)
            cliens.save()
            self.stdout.write(f'{cliens}')
