
from django.urls import path
from. import views

urlpatterns = [
    path('', views.home, name='index'),  # Add name='index' here
    path('about/', views.about, name='about'),
    path('product_list/', views.product_list, name='product_list'),  # Note the name 'product_list'
    path('contact/', views.contact, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('products/<int:pk>/', views.product_details, name='product_detail'),
]