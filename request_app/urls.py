from django.urls import path
from request_app import views


app_name = 'request_app'

urlpatterns = [
    path('get/', views.process_get, name='get-view'),
    path('info/', views.user_form, name='user-info'),
    path('file-upload/', views.upload_file, name='file-upload'),
]