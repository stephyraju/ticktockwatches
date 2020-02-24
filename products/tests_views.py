from django.test import TestCase, Client

c=Client()

# Create your tests here.
class TestProductViews(TestCase):
  
    def test_index_page(self):
        page = c.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_all_products_page(self):
        page = c.get("/products/products")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")