from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account', views.account_view, name="account"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
]