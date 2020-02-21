from django.test import TestCase, Client

c=Client()

class TestHomeViews(TestCase):

    def test_about_page(self):
        page = c.get("/home/about/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "about.html")

    def test_delivery_page(self):
        page = c.get("/home/delivery/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "delivery.html") 

    def test_faqs_page(self):
        page = c.get("/home/faqs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "faqs.html") 

    def test_return_page(self):
        page = c.get("/home/return/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "return.html") 

    def test_contact_page(self):
        page = c.get("/home/contact/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "contact.html") 