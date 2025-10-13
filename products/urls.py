from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name="product_list"),
    path("export_excel/", views.export_products_excel, name="export_excel"),
]