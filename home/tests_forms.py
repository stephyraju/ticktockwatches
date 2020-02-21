from django.test import TestCase
from .forms import ContactForm

class TestHomeForms(TestCase):

    def test_form_can_be_submitted_with_all_the_fields_filled(self):
        form = ContactForm({
            'name' :'name',
            'email':'email@gmail.com',
            'subject':'matter',
            'message':'message'
            })
        self.assertTrue(form.is_valid())

    def test_form_cannot_be_submitted_email_empty(self):
        form = ContactForm({
            'name' :'name',
            'email':'',
            'subject':'matter',
            'message':'message'
            })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'],[u'This field is required.'])

    def test_form_cannot_be_submitted_message_empty(self):
        form = ContactForm({
            'name' :'name',
            'email':'email@gmail.com',
            'subject':'matter',
            'message':''
            })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['message'],[u'This field is required.'])

    def test_form_cannot_be_submitted_name_empty(self):
        form = ContactForm({
            'name':'',
            'email':'email@gmail.com',
            'subject':'matter',
            'message':'message'
            })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'],[u'This field is required.'])