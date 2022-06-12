from django.urls import path

from posts import views

urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
    path('user/<int:pk>', views.DetailedUserView.as_view(), name='user_page'),
    path('users/', views.users, name='users'),
]
