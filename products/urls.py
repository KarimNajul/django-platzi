from django.urls import path
from .views import ProductFormView, ProductListView


urlpatterns = [
    path('agregar/', ProductFormView.as_view(), name="add_product"),
    path('', ProductListView.as_view(), name="list_product")
]