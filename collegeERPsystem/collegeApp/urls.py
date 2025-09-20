from django.urls import path
from .import views

urlpatterns = [
    path("",views.Authentications.signin, name='signin'),
    path("index/",views.Home.index, name='index'),
]