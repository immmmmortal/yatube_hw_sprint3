from http.client import HTTPResponse

import kwargs as kwargs
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from posts.models import Group, Post


class HomeView(ListView):
    model = Group
    template_name = 'home_page.html'


class DetailedGroupView(DetailView):
    model = Group
    template_name = 'group_page.html'

    def get_context_data(self, **kwargs):
        context = super(DetailedGroupView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(group_id=self.get_object())
        return context
