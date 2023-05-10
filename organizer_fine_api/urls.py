"""
URL configuration for organizer_fine_api project.

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
from django.urls import path, include, re_path
from knox import views as knox_views
from rest_framework import routers
from core.views import RevenueSpendingView, RegisterAPI, LoginAPI


api_router = routers.DefaultRouter()
api_router.register(r"revenue_spending", RevenueSpendingView, basename='revenue_spending')

urlpatterns = [
    
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/', include(api_router.urls)),
    path('admin/', admin.site.urls, name='Admin')
    # path('rest_auth/', include('rest_auth.urls')),
    # re_path('rest_auth/registration/', include('rest_auth.registration.urls'))
]
