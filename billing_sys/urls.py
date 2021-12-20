from django.urls import path
from . import views

urlpatterns = [
    path('', views.billing_sys, name = 'index'),
    path('user_details/', views.user_details, name = 'user_details'),
]