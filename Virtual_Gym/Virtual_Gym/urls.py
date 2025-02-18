"""
URL configuration for Virtual_Gym project.

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
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls", namespace="blog")),
    path("tutorials/", include("tutorials.urls", namespace="tutorials")),
    path("practice/", include("practice.urls", namespace="practice")),
    path("store/", include("store.urls", namespace="store")),
    # The url below will handle our auth page using django, these two urls are necessary in this order
    #Reference of LOGIN_REDIRECT_URL & LOGOUT_REDIRECT_URL in the settings.py is necessary to make 'login' and 'logout' easier just using those words in the links
    path("users/", include("django.contrib.auth.urls")),
    path("users/", include("users.urls")),
]
