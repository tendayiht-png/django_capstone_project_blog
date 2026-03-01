"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views
from django.urls import path, include
from .. import views
from hello_world import views as index_views

from django_math_land_project.my_project import views as index_views

urlpatterns = [
    path('hello/', index_views.index, name='index'),
    path('add/', views.add_numbers, name='add_numbers'),
    path('admin/', admin.site.urls),
    path('save-score/', views.save_score, name='save_score'),
    path('hello/', views.math_game, name='math_game'),
]




