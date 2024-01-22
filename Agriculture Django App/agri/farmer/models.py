from django.db import models

# Create your models here.

class Farmer(models.Model):
    farmer_name = models.CharField(max_length=30, blank=False)
    farmer_email = models.EmailField(max_length=200,unique=True)
    farmer_phone = models.CharField(max_length=200)
    farmer_address = models.CharField(max_length=2000)
    farmer_password = models.CharField(max_length=200)
    farmer_profile_pic = models.ImageField(upload_to='profile_pics/',blank=True,default='profile_pics/default.jpeg')
    def __str__(self):
        return self.farmer_name
    
class Catogery(models.Model):
    product_catogery = models.CharField(max_length=200)
    def __str__(self):
        return self.product_catogery
    
class SubCatogery(models.Model):
    product_subcatogery = models.CharField(max_length=200)
    falls_under_category = models.ForeignKey(Catogery,on_delete=models.CASCADE)
    def __str__(self):
        return self.product_subcatogery

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    product_description = models.CharField(max_length=2000)
    product_image = models.ImageField(upload_to='product_images/',blank=True,default='product_images/default.jpeg')
    product_catogery = models.ForeignKey(Catogery,on_delete=models.CASCADE)
    product_subcatogery = models.ForeignKey(SubCatogery,on_delete=models.CASCADE)
    product_unit = models.CharField(max_length=20)
    def __str__(self):
        return self.product_name
    