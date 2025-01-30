from django.urls import path

from .views import MyOrderView, CreateOrderProductView


urlpatterns = [
    path("mi-orden", MyOrderView.as_view(), name="my_order"),
    path("aregar-producto", CreateOrderProductView.as_view(), name="add_product"),
]
