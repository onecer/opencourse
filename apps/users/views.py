# coding: utf-8
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.views.generic.base import View
from django.db.models import Q

from .models import UserProfile
from .forms import LoginForm, RegisterForm

# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def login_view(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = authenticate(request, username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {"msg": "用户或密码错误"})
    if request.method == 'GET':
        return render(request, 'login.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(request, username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {"msg": "用户或密码错误"})
        else:
            return render(request, 'login.html', {"login_form": login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request=request, template_name='register.html', context={"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_profile = UserProfile()
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(password=pass_word)
        else:
            return render(request=request, template_name='register.html', context={"register_form": register_form})
