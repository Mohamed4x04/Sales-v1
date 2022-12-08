from django import forms
from .models import AddProduct



class ProductForm(forms.ModelForm):
    class Meta:
       model = AddProduct
       fields = '__all__'
       exclude = ('date_add',)
    
    