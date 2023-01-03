from django import forms
from .models import AddProduct , Category , Storage



class ProductForm(forms.ModelForm):
    class Meta:
       model = AddProduct
       fields = '__all__'
       exclude = ('date_add',)
    


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category    
        fields = '__all__'
        
        
        
class StorageForm(forms.ModelForm):
    class Meta:
        model= Storage
        fields= '__all__'        