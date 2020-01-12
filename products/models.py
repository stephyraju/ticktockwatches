from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    Mens_Watches = "Mens Watches"
    Ladies_Watches = "Ladies Watches" 
    Kids_watches = "Kids Watches"
    Rolex = "Rolex"
    Timex = "Timex"
    Ted_Baker = "Ted Baker"
    Tissot =  "Tissot"
    Michael_Kors = "Michael Kors"
    Lacoste =  "Lacoste"
    Lotus =  "Lotus"
    Hugo =  "Hugo"
    Gucci = "Gucci"
    Diesel =  "Diesel"
    
    CATEGORY_CHOICES = [
        ("Mens Watches", "Mens Watches" ),
        ("Ladies Watches", "Ladies Watches"),
        ("Kids Watches", "Kids Watches")
    ]

    BRAND_CHOICES = [
        (Rolex, "Rolex"),
        (Timex, "Timex"),
        (Ted_Baker, "Ted Baker"),
        (Tissot, "Tissot"),
        (Michael_Kors, "Michael Kors"),
        (Lacoste, "Lacoste"),
        (Lotus, "Lotus"),
        (Hugo, "Hugo"),
        (Gucci, "Gucci"),
        (Diesel, "Diesel")
    ]
    
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="Rolex"
    )

    brand = models.CharField(
        max_length=20,
        choices=BRAND_CHOICES,
        default=Rolex,
    )

    title = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    featured = models.BooleanField(default=False)
    bestseller = models.BooleanField(default=False)
    def __str__(self):
        return self.name




# class Product(models.Model):

#     
#     name = models.CharField(max_length=254, default='')
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     image = models.ImageField(upload_to="images", blank=True, null=True)
    
#     def __str__(self):
#         return self.name