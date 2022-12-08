from django.shortcuts import render
from .models import AddProduct 
from .forms import ProductForm
from django.shortcuts import redirect

# Create your views here.







def add_product(request):
    product = AddProduct.objects.all()
    return render(request, 'products/product_list.html' , {'product':product})





def product_detail(request,id):
    product_detail = AddProduct.objects.filter(id=id)
    return render (request, 'products/product_detail.html' ,{'product_detail':product_detail} )


def new_product(request):
    if request.method =="POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
                
        
    return render (request, 'products/new_product.html' , {'form':form})


def edit_product(request,id):
    product = AddProduct.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            
    else:
        form = ProductForm(instance=product)
        
        
    return render(request, 'products/new_product.html' , {'form':form})    





def delete_product(request,id):
    product = AddProduct.objects.get(id=id)
    product.delete()
    return redirect('/products')

    
          
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    