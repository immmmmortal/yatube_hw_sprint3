from django.urls import path
from django.conf.urls import handler404, handler500
from posts import views

handler404 = 'posts.views.page_not_found'  # noqa
handler500 = 'posts.views.server_error'  # noqa

urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
    path('sign_up/', views.SignUpUserView.as_view(), name='sign_up'),
    path('user/<int:pk>', views.DetailedUserView.as_view(), name='user_page'),
    path('users/', views.users, name='users'),
]
