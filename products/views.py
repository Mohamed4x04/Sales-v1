from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import AddProduct 
# Create your views here.








class ProductList(ListView):
    model = AddProduct
    
    
    
class ProductDetail(DetailView):
    model = AddProduct    