
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.main),
    path('about/', views.register),
    path('showdata/', views.writedata),
]


