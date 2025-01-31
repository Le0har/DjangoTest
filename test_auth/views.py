from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from test_auth.models import Profile


class ProfileView(TemplateView, LoginRequiredMixin):
    template_name = 'test_auth/profile.html'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'test_auth/register.html'
    success_url = reverse_lazy('test_auth:profile')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return response


def login_view(request): 
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/shop/')
        return render(request, 'test_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/shop/')
    return render(request, 'test_auth/login.html', {'error': 'Invalid login credentials!'})


def logout_view(request):
    logout(request)
    return redirect(reverse('test_auth:login'))


class TestLogoutView(LogoutView):
    next_page = reverse_lazy('test_auth:login')


def set_cookie_view(request):
    response = HttpResponse('Cookie set')
    response.set_cookie('new', 'info', max_age=3600)
    return response


def get_cookie_view(request):
    value = request.COOKIES.get('new', 'default info')
    return HttpResponse(f'Cookie value: {value}')


@permission_required('test_auth.view_profile', raise_exception=True)
def set_session_view(request):
    request.session['new'] = 'new info'
    return HttpResponse('Session set')


@login_required
def get_session_view(request):
    value = request.session.get('new', 'default info')
    return HttpResponse(f'Session value: {value}')
