from django.contrib.auth.views import LoginView
from django.urls import path
from test_auth import views


app_name = 'test_auth'

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
    # path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(
        template_name='test_auth/login.html',
        redirect_authenticated_user=True
        ), name='login'),
    path('cookie/get/', views.get_cookie_view, name='cookie-get'),
    path('cookie/set/', views.set_cookie_view, name='cookie-set'), 
    path('session/get/', views.get_session_view, name='session-get'), 
    path('session/set/', views.set_session_view, name='session-set'),  
]