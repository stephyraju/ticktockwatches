from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm

class TestAccountsForms(TestCase):


    def setUp(self):
        self.registration_form = UserRegistrationForm({
            'first_name':'first_name',
            'last_name':'last_name', 
            'email':'email@gmail.com', 
            'username':'username', 
            'password1':'pass123word', 
            'password2':'pass123word'})
    

    def test_user_cannot_register_without_filling_out_all_fields(self):
        form = UserRegistrationForm({
            'first_name':'',
            'last_name':'', 
            'email':'', 
            'username':'', 
            'password1':'', 
            'password2':''})
        self.assertFalse(form.is_valid())  
        self.assertEqual(form.errors['first_name'],[u'This field is required.'])
        self.assertEqual(form.errors['last_name'],[u'This field is required.'])
        self.assertEqual(form.errors['email'],[u'This field is required.'])
        self.assertEqual(form.errors['username'],[u'This field is required.'])
        self.assertEqual(form.errors['password1'],[u'This field is required.'])
        self.assertEqual(form.errors['password2'],[u'This field is required.'])


    def test_user_can_register_filling_all_the_fields(self):
        self.assertTrue(self.registration_form.is_valid())


    def test_user_can_login_with_username_and_password(self):
        form = UserLoginForm({'username':'username', 'password':'password'})
        self.assertTrue(form.is_valid())


    def test_user_cannot_login_without_username(self):
        form = UserLoginForm({'username':'', 'password':'password'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'],[u'This field is required.'])


    def test_user_cannot_login_without_password(self):
        form = UserLoginForm({'username':'username', 'password':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'],[u'This field is required.'])


    def test_password_dont_match(self):
        form = UserRegistrationForm({
            'first_name':'first_name',
            'last_name':'last_name', 
            'email':'email@gmail.com', 
            'username':'username', 
            'password1':'1234hnmff', 
            'password2':'pass123word'})
        self.assertFalse(form.is_valid())  
        self.assertEqual(form.errors['password2'],[u'The passwords must match'])


    def test_both_passwords_are_filled(self):
        form = UserRegistrationForm({
            'first_name':'first_name',
            'last_name':'last_name', 
            'email':'email@gmail.com', 
            'username':'username', 
            'password1':'', 
            'password2':'padjdnddd'})
        self.assertFalse(form.is_valid())  
        self.assertEqual(form.errors['password2'],[u'Please confirm your password'])


    def test_email_has_to_be_unique_when_register(self):
        self.assertTrue(self.registration_form.is_valid())
        self.registration_form.save()

        form2 = UserRegistrationForm({
            'first_name':'first_name2',
            'last_name':'last_name2', 
            'email':'email@gmail.com', 
            'username':'username2', 
            'password1':'pass123word', 
            'password2':'pass123word'})
        
        self.assertFalse(form2.is_valid())
        self.assertEqual(form2.errors['email'],[u'Email address must be unique'])


    def test_username_has_to_be_unique_when_registering(self):
        self.assertTrue(self.registration_form.is_valid())
        self.registration_form.save()

        form2 = UserRegistrationForm({
            'first_name':'first_name2',
            'last_name':'last_name2', 
            'email':'test@mail.cm', 
            'username':'username', 
            'password1':'12345abcds', 
            'password2':'12345abcds'})
            
        self.assertFalse(form2.is_valid())
        self.assertEqual(form2.errors['username'],[u'A user with that username already exists.'])