from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
# Create your models here.





class AddProduct(models.Model):
    name = models.CharField(_("Product Name") , max_length=50)
    parcode = models.ForeignKey('ParcodePrint' , verbose_name=_("Parcode") , related_name='product_parcode' , on_delete=models.SET_NULL , null=True , blank=True)
    category = models.ForeignKey('Category' , verbose_name=_("Category") , related_name='product_category' , on_delete=models.SET_NULL , null=True , blank=True)
    storage = models.ForeignKey('Storage' , verbose_name=_("Storage") , related_name='product_storage' , on_delete=models.SET_NULL , null=True , blank=True)
    purchasing_price = models.FloatField(_("Purchasing Price") , default=0)
    order_limit = models.IntegerField(_("Order Limit") , default=0)
    sell_price = models.FloatField(_("Sell Price") , default=0)
    date_add = models.DateTimeField(_("Date Add") , null=True , blank=True)
    image = models.ImageField(_("Product Image") , upload_to='products/' , null=True , blank=True)
    quantity = models.IntegerField(_("Quantity") , default=0)
    notes = models.CharField(_("Notes") , max_length=100 )
    
    
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(_("Category Name") , max_length=50)
    
    
    def __str__(self):
        return self.name




class Storage(models.Model):
    name = models.CharField(_("Storage") , max_length=50)
    
    
    def __str__(self):
        return self.name    
    
    
class AddQuantity(models.Model):
    parcode = models.ForeignKey('ParcodePrint' , verbose_name=_("Parcode") , related_name='quantity_parcode' , on_delete=models.SET_NULL , null=True , blank=True)
    quantity = models.ForeignKey(AddProduct , verbose_name=_("Quantity") , related_name='product_quantity' , on_delete=models.SET_NULL , null=True , blank=True)
    name = models.CharField(_("Name") , max_length=30)
    
    def __str__(self):
        return self.name   
    
    
class ParcodePrint(models.Model):
    parcode = models.IntegerField(_("Parcode") , default=0)
    product_name = models.CharField(_("Name") , max_length=30)    
    quantity = models.ForeignKey(AddQuantity , verbose_name=_("Quantity") , related_name='quantity_parcode1' , on_delete=models.SET_NULL , null=True , blank=True)

    def __str__(self):
        return self.product_name   
    
    
        
class ProductImage(models.Model):
    product = models.ForeignKey(AddProduct , verbose_name=_("Product") , related_name='product_image' , on_delete=models.CASCADE)  
    image = models.ImageField(_("Image") , upload_to='product/')      
    
       