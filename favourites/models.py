from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     user = models.CharField(max_length=30)
#     email = models.EmailField()

#     def __str__(self):
#         return "%s %s" % (self.user)

class Favourites(models.Model):
    # id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product, null=False)

    # def __str__(self):
    #     return self.id
    def __unicode__(self):
        return self.user

    class Meta:
        ordering = ['-id']
