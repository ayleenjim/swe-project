from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.sites.url),
    path('', views.home, name= 'home'),
]