from http.client import HTTPResponse

import kwargs as kwargs
from django.contrib.auth.models import User
from django.db.models import Prefetch
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from posts.forms import AddPostForm
from posts.models import Group, Post, Author


class HomeView(ListView):
    model = Group
    template_name = 'home_page.html'


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
