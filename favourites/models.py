from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# class Favourites(models.Model):
#     # id = models.IntegerField(primary_key=True)
#     user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
#     product =  models.ForeignKey(Product, null=False)

#     def __str__(self):
#         return self.favourites

#     class Meta:
#         ordering = ['-id']

# class Favourites(models.Model):

#         user = models.ForeignKey(User,null=True, blank=True)
#         product = models.ForeignKey(Product, null=False)
#         # favourite = models.ManyToManyField(User, related_name='favourite', blank=True)

#         class Meta:
#            ordering = ['-id']

#         def __str__(self):
#             return self.favourites
