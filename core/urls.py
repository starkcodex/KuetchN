
from . import views
from django.urls import path, include

from core.customer import views as customer_views
from core.courier import views as courier_views

customer_urlpatterns = [
    path('', customer_views.home, name='home'),
    path('profile/', customer_views.profile_page, name='profile'),
    
]

courier_urlpatterns = [
    path('', courier_views.home, name='home')
]


urlpatterns = [
    path('', views.hero_page, name='hero'),
    path('home/', views.home, name='home'),
    path('customer/', include((customer_urlpatterns, 'customer'))),
    path('courier/', include((courier_urlpatterns, 'courier')))
]

