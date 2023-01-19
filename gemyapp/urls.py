from django.urls import path
from .views import product_list , product_detail , category_list , brand_list ,brand_detail

app_name = 'gemyapp'


urlpatterns = [
    path('' , product_list , name='product_list'),
    path('<int:id>/edit' , product_detail , name='product_detail'),
    path('category/' , category_list , name='category_list'),
    path('brand/' , brand_list , name='brand_list'),
    path('<int:id>/edit_brand' , brand_detail , name='brand_detail'),
    
]
