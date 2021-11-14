from django.urls import path
from . import views

urlpatterns = [
    path('', views.billing_sys),
    path('user_details/', views.user_details),
]