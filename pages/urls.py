from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('service/', views.service_view, name='service'),
]