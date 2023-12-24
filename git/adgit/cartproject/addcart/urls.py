from .import views
from django.urls import path
app_name='addcart'
urlpatterns = [
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('',views.Cart_detail,name='Cart_detail'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('trash_remove/<int:product_id>/',views.trash_remove,name='trash_remove'),
    ]