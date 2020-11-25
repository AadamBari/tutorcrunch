import json

from django.core.management import BaseCommand

from dev_test import settings
from dev_test.main.models import Product


class Command(BaseCommand):
    def handle(self, **kwargs):
        with open(settings.BASE_DIR + '/products.json') as f:
            product_data = json.load(f)
            for name, price in product_data.items():
                Product.objects.get_or_create(name=name, price=price)
