from django.contrib import admin
from .models import Farmer,Catogery,SubCatogery,Product
# Register your models here.
admin.site.register(Farmer)
admin.site.register(Catogery)
admin.site.register(SubCatogery)
admin.site.register(Product)