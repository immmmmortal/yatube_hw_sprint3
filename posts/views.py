from http.client import HTTPResponse

import kwargs as kwargs
from django.conf.global_settings import LOGOUT_REDIRECT_URL
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Prefetch
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from posts.models import Group, Post, Author

from posts.forms import AddPostForm
from yatube.settings import LOGIN_REDIRECT_URL


def page_not_found(request: HttpRequest, exception: Exception):
    return render(
        request,
        {'path': request.path},
        'misc/404.html',
        status=404
    )


def server_error(request):
    return render(request, "misc/500.html", status=500)


class SignUpUserView(CreateView):
    model = Author
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class HomeView(ListView):
    model = Group
    template_name = 'home_page.html'


class LoginUserView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('home_page')


class LogoutView(LogoutView):
    LOGIN_REDIRECT_URL = reverse_lazy('login')
    LOGOUT_REDIRECT_URL = reverse_lazy('login')


class DetailedGroupView(DetailView):
    model = Group
    template_name = 'group_page.html'


def add_post(request: HttpRequest) -> HttpResponseRedirect:
    if request.POST:
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, 'add_post.html', {'form': form})

    return render(request, 'add_post.html', {'form': AddPostForm})


class DetailedUserView(DetailView):
    model = Author
    template_name = 'user_page.html'


def users(request: HttpRequest) -> HttpResponseRedirect:
    users_list = User.objects.all().select_related('author')
    return render(request, 'users.html', {'users': users_list})
