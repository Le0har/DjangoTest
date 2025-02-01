from django.urls import path
from test_api import views


app_name = 'test_api'

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('groups/', views.GroupListAPIView.as_view(), name='groups'),
]