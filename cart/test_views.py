from django.test import Client, TestCase
from django.contrib.auth.models import User
from products.models import Product

c=Client()

class TestCartViews(TestCase):

    def setUp(self):
        '''In order to test the cart the user needs to be logged in'''
        
        self.first_name = 'first_name',
        self.last_name = 'last_name', 
        self.email = 'email@test.com', 
        self.username = 'username', 
        self.password1 ='password432', 
        self.password2 = 'password432'  
        login = c.login(username="username", password="password432")
        

    def test_cart_cannot_be_access_user_loggedout(self):
        page = c.logout()      
        page = c.get("/cart/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertRedirects(page, '/accounts/login/?next=/cart/')
    
    def test_cart_page_loggedin_user(self):
        page = c.get("/cart")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")