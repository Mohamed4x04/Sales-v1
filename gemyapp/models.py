from django.db import models

# Create your models here.



class Products(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category' , related_name='product_category' ,on_delete=models.SET_NULL , null=True , blank=True)
    brand = models.ForeignKey('Brand' , related_name='product_brand' , on_delete=models.SET_NULL , null=True , blank=True)
    image = models.ImageField(upload_to='products/')
    
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/')
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='brand/')
    
    
    def __str__(self):
        return self.name        
    