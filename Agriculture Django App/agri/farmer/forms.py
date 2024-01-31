from django import forms
from .models import Farmer,Product,Catogery,SubCatogery

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ('farmer_name','farmer_email','farmer_phone','farmer_address','farmer_password')
        exclude = ('farmer_profile_pic',)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name','product_price','product_quantity','product_description','product_image','product_catogery','product_subcatogery','product_unit')