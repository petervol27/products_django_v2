from django.urls import path
from . import views

urlpatterns = [path("", views.products_list, ),path('<int:id>',views.product_details)]
