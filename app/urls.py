from django.urls import path
from . import views 


urlpatterns = [
    path("", views.index, name= "index"),
    path("cart", views.cart, name= "cart"),
    path("checkout", views.checkout, name= "checkout"),
    path("main", views.main, name= "main")

]
