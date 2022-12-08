from django.urls import path
from .views import add_product , product_detail , new_product , edit_product , delete_product

app_name = 'products'

urlpatterns = [
    path('' ,add_product , name='add_product' ),
    path('<int:id>' ,product_detail , name='product_detail' ),
    path('<int:id>/edit' ,edit_product , name='edit_product' ),
    path('<int:id>/delete' ,delete_product , name='delete_product' ),
    path('new_product' , new_product , name='new_product'),
    
]



