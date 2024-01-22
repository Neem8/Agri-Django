from django.db import models

# Create your models here.


class Admin(models.Model):
    admin_name = models.CharField(max_length=30, blank=False)
    admin_email = models.EmailField(max_length=200,unique=True)
    admin_phone = models.CharField(max_length=200)
    admin_address = models.CharField(max_length=2000)
    admin_password = models.CharField(max_length=200)
    admin_profile_pic = models.ImageField(upload_to='profile_pics/',blank=True,default='profile_pics/default.jpeg')
    def __str__(self):
        return self.admin_name