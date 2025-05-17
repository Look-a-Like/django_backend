"""
URL configuration for tradesmate_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.http import HttpResponse  # Add this import

# Sentry debug view
def trigger_error(request):
    division_by_zero = 1 / 0
    return HttpResponse("This won't be displayed")

# Add a simple index view
def index(request):
    return HttpResponse("Hello, world. Welcome to TradesMate!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
    path('', index, name='index'),  # Add this URL pattern for the homepage
]