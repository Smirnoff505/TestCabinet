from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import registration, show_login_password, user_login

app_name = UsersConfig.name

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('registration/show-login-password/', show_login_password, name='show_login_password'),
    path('lk/', user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
