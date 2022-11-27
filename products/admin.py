from django.contrib import admin
from .models import AddProduct , Category , Storage , AddQuantity , ParcodePrint , ProductImage
# Register your models here.




class ProductImageInline(admin.TabularInline):
    model = ProductImage
    				                                                
                                                                   
class AddProductAdmin(admin.ModelAdmin):
    inline = [ProductImageInline]




admin.site.register(AddProduct,AddProductAdmin)
admin.site.register(Category)
admin.site.register(Storage)
admin.site.register(AddQuantity)
admin.site.register(ParcodePrint)
admin.site.register(ProductImage)
