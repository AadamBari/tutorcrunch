from django.db import models


class Product(models.Model):
    name = models.CharField('Name', max_length=20)
    price = models.DecimalField('Amount paid', decimal_places=2, max_digits=4)

    def __str__(self):
        return self.name


class Order(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)
    amount_paid = models.DecimalField('Amount paid', decimal_places=2, max_digits=256)
