from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from accounts.forms import UserRegistrationForm

User = get_user_model()

c=Client()
class TestViews(TestCase):

    def setUp(self):
        self.registration_form = UserRegistrationForm({
            'first_name':'first_name',
            'last_name':'last_name', 
            'email':'test@email.com', 
            'username':'username', 
            'password1':'pass123word', 
            'password2':'pass123word'})

    def test_get_registerPage(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")
    
    def test_get_profilePage(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
    
    def test_get_loginPage(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_user_cannot_login_if_not_registered(self):
        self.registration_form.save()  
        login_ok = c.login(username="anotherusername", password="12345passw")
        self.assertFalse(login_ok)
        
    def test_login_functionality_when_user_is_registered(self):
        self.registration_form.save()  
        login_ok = c.login(username="username", password="pass123word")
        self.assertTrue(login_ok)

    def test_logged_in_user_redirected_to_index_when_try_to_log_in_again(self):
        self.registration_form.save()
        login_ok = c.login(username="username", password="pass123word")
        self.assertTrue(login_ok)
        page = c.get("/accounts/login/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertRedirects(page, '/products/')

    def test_logout_functionality(self):
        self.registration_form.save()        
        login_ok = c.login(username="username", password="pass123word")
        self.assertTrue(login_ok)
        page = c.get("/accounts/logout/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertRedirects(page, '/products/')

    def test_user_can_login_using_email(self):
        self.registration_form.save()
        login_ok = c.login(username="test@email.com", password="pass123word")
        self.assertTrue(login_ok)