from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .storages import *


class HomeView(TemplateView):
    template_name = "mainapp/home.html"
    context = {'title': 'Главная'}


class Login_url(TemplateView):
    template_name = "mainapp/login_url.html"
    context = {'title': 'Главная'}


class Login_no_sso_url(TemplateView):
    template_name = "mainapp/login_no_sso_url.html"
    context = {'title': 'Главная'}


class Callback_url(TemplateView):
    template_name = "mainapp/callback_url.html"
    context = {'title': 'Главная'}


class Logout_url(TemplateView):
    template_name = "mainapp/logout_url.html"
    context = {'title': 'Главная'}


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'mainapp/login_2.html'
    # success_url = 'mainapp/home_2.html'

    def get_success_url(self):
        return reverse_lazy('home')


def user_data(request):
    user_login = request.user
    # print('passw:', request.user.password)
    # print('login:', request.user.username)

    sn, givenName, mail = ldap_connection(user_login)
    context = {
        'title': 'Данные из AD',
        "username": sn,
        "first_name": givenName,
        "last_name": sn,
        "email": mail,

    }
    return render(request, 'mainapp/user-data.html', context)


def user_mail(request):
    username = request.user.password
    password = request.user.username

    mail_list = check_mailbox(username, password, "ALL")
    # print(mail_list)
    context = {"mail_list": mail_list,
               'title': 'Почта',
               }
    return render(request, 'mainapp/user-mail.html', context=context)


# def logout_user(request):
#     logout(request)
#     return redirect('oauth2/login_no_sso/')
    # return redirect('login_no_sso')