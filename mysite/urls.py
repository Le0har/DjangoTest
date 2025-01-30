from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shopapp.urls')),
    path('req/', include('request_app.urls')),
    path('auth/', include('test_auth.urls')),
]
