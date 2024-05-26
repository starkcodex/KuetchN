

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hero_page, name='hero'),
    path('home/', views.home, name='home'),
    path('customer/', views.customer, name='customer'),
    path('courier/', views.courier, name='courier')
]
