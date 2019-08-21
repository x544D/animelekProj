"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from users.views import members_view
from pages.views import home_view, contact_view
from animes.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view),
    path('contact/', contact_view ),
    path('admin/', admin.site.urls),
    path('members/', members_view, name='members'),
    path('animes/<int:_id>/',single_animes_view),
    path('animes/',list_animes_view),

]
