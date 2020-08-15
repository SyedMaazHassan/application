from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, auth
# Create your models here.


class categories(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class sub_categorie(models.Model):
    sub_category_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.sub_category_name

class sub_sub_categorie(models.Model):
    sub_sub_category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.sub_sub_category_name

class available_item(models.Model):
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(sub_categorie, on_delete=models.CASCADE)
    sub_sub_category = models.ForeignKey(sub_sub_categorie, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='photos')
    item_name = models.CharField(max_length=255)
    price_per_unit = models.FloatField()
    installed_vendor = models.CharField(max_length=3, choices=(("YES", "YES"), ("NO", "NO")))
