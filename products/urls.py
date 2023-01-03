from django.urls import path
from .views import add_product , product_detail , new_product , edit_product , delete_product ,category_list, category_detail, brand_list, brand_detail, storage_list

app_name = 'products'

urlpatterns = [
    path('' ,add_product , name='add_product' ),
    path('new_product' , new_product , name='new_product'),
    path('<int:id>' ,product_detail , name='product_detail' ),
    path('<int:id>/edit' ,edit_product , name='edit_product' ),
    path('<int:id>/delete' ,delete_product , name='delete_product' ),
    
    path('category/' , category_list , name='category_list'),
    path('<int:id>/edit_category' ,category_detail, name='category_detail'),
    
    path('brand/', brand_list, name='brand_list'),
    path('<int:id>/edit_brand', brand_detail, name='brand_detail'),
    
    path('storage/', storage_list, name='storage_list')
    
    
]



