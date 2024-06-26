from core import views
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from django.conf.urls.static import static  
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    # social auth url configuration.
    path('', include('social_django.urls', namespace='social')),
    path('', include('core.urls')),
    
    # authentication paths
    path('sign-up/', views.sign_up),
    path('sign-in/', auth_views.LoginView.as_view(template_name="auth/sign_in.html")),
    path('sign-out/', auth_views.LogoutView.as_view(next_page="/")),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)