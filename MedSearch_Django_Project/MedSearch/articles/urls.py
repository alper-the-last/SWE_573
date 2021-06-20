from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.registerPage, name="Home"),

    path('detail', views.retrieve_article_data, name="article"),
    path('results', views.Results, name="Results"),
    path('register', views.registerPage, name="Register"),
    path('login', views.loginPage, name="Login"),
    path('logout', views.logoutPage, name="Logout"),


]
