from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_user = models.BooleanField(default=False)

class userlogin(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE,related_name='user',null=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=30)
    address = models.TextField(max_length=200)
    phone = models.IntegerField(null=True,blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True)
    Product_name = models.CharField(max_length=100)
    Product_description = models.CharField(max_length=200)
    Product_quantity = models.CharField(max_length=50)
    Product_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user
