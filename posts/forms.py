from django import forms
from django.forms import ModelForm

from posts.models import Post, Group, Author


class AddPostForm(ModelForm):
    title = forms.CharField(max_length=48)
    description = forms.CharField(max_length=1024)
    image = forms.ImageField()
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    
    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'group', 'author']
