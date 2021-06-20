"""MedSearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include('articles.urls'), name="Home"),
    path('Admin/', admin.site.urls),

    path('Article/<int:pk>', include('articles.urls'), name="article"),
    path('Results', include('articles.urls'), name="Results"),

    path('Register', include('articles.urls'), name="Register"),
    path('Login', include('articles.urls'), name="Login"),
    path('Logout', include('articles.urls'), name="Logout"),
]
