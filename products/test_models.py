from django.test import TestCase
from .models import Product

class ProductTests(TestCase):
    
    """ Test Product model returns product title """
    def test_str(self):
         product = Product(title="Test TickTock")
         self.assertEqual(str(product), product.title)

    