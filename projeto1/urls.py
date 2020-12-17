from django.urls import path
from . import views

urlpatterns = [
    path('', views.testeview),
    path('add', views.testeadd),
]
