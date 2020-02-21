from django.test import Client, TestCase
from django.contrib.auth.models import User
from products.models import Product

c=Client()

class TestCartViews(TestCase):

    def setUp(self):
        """ Creates user in test database to get login status """

        self.user = User.objects.create_user(
            username='username', email='test@email.com', password="pass123word"
        )
        
    def test_response_status_200(self):
        """ Test that Logged in user is not redirected from cart page """

        c.login(username='username', password="pass123word")
        response = c.get('/cart/')
        self.assertEqual(response.status_code, 200)

    def test_cart_cannot_be_access_user_loggedout(self):
        """ Test that logged out user will redirects to login page"""

        page = c.logout()      
        page = c.get("/cart/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertRedirects(page, '/accounts/login/?next=/cart/')