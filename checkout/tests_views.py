from django.test import TestCase, Client
from django.contrib.auth.models import User
from products.models import Product
from .models import Order, OrderLineItem

c=Client()

class TestCartViews(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(
            username='username', email='test@email.com', password="pass123word")

    # def test_cart_page_authenticated_user(self):
    #     c.login(username="username", password="pass123word")
    #     page = c.get('/checkout/')
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page.status_code, "checkout.html")

    def test_cart_cannot_be_access_by_loggedout_user(self):
        page = c.logout()      
        page = c.get("/checkout/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertRedirects(page, '/accounts/login/?next=/checkout/')