from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.fetch_carts,
    ), path("<str:username>",views.fetch_cart)
]
