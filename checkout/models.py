from django.db import models
import datetime
from products.models import Product

# Create your models here.

class Order(models.Model):

    """
    Model to store  customer information, shipping address and
    date ordered.
    """

    full_name = models.CharField(max_length=50, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=40, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    date_ordered = models.DateField(default=datetime.date.today, null=True)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):

    """
    Model to store individual order items, the  Product and the quantity
    ordered.
    
    """

    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.name, self.product.price)