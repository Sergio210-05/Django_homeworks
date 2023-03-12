import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        Phone().clean()
        for phone in phones:
            phone['slug'] = phone['name'].replace(' ', '-')
            print(phone)
            Phone(**phone).save()

        return phones

