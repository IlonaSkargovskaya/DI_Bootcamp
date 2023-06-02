from django.urls import path
from . import views

# (вызываем созданную там функцию)
urlpatterns = [
    path('customers/', views.all_customers, name="all_customers"),
    path('customer/<int:pk>', views.customer, name="customer"),
    path('customer/add', views.add_customer, name="add_customer")
]