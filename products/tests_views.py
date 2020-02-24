from django.test import TestCase, Client
from .models import Product

c=Client()

# Create your tests here.
class TestProductViews(TestCase):
  
    def test_index_page(self):
        page = c.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_all_products_page(self):
        page = c.get("/products_list/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")
    
    def test_kids_watch_redirects_to_products_page(self):
        page = c.get("/products/view_kidswatch/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_mens_watch_redirects_to_products_page(self):
        page = c.get("/products/view_menswatch/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_ladies_watch_redirects_to_products_page(self):
        page = c.get("/products/view_ladieswatch/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_rolex_watch_redirects_to_products_page(self):
        page = c.get("/products/view_rolex/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_timex_watch_redirects_to_products_page(self):
        page = c.get("/products/view_timex/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_tedbaker_watch_redirects_to_products_page(self):
        page = c.get("/products/view_tedbaker/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_tissot_watch_redirects_to_products_page(self):
        page = c.get("/products/view_tissot/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_michaelkores_watch_redirects_to_products_page(self):
        page = c.get("/products/view_michaelkores/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_lorus_watch_redirects_to_products_page(self):
        page = c.get("/products/view_lorus/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_lacoste_watch_redirects_to_products_page(self):
        page = c.get("/products/view_lacoste/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_citizen_watch_redirects_to_products_page(self):
        page = c.get("/products/view_citizen/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

