from django.shortcuts import render
from .models import Products , Category , Brand
# Create your views here.




def product_list(request):
    product_list = Products.objects.all()
    return render(request, 'gemyapp/product_list.html', {'product_list':product_list})



def product_detail(request,id):
    product_detail = Products.objects.get(id=id)
    return render(request, 'gemyapp/product_detail.html', {'product_detail':product_detail})


def category_list(request):
    category_list = Category.objects.all()
    return render(request, 'gemyapp/category_list.html', {'category_list':category_list})


def brand_list(request):
    brand_list = Brand.objects.all()
    return render(request, 'gemyapp/brand_list.html' , {'brand_list':brand_list})


def brand_detail(request,id):
    brand_detail = Brand.objects.filter(id=id)
    return render (request, 'gemyapp/brand_detail.html', {'brand_detail':brand_detail})
