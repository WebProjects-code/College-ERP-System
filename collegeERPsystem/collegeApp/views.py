from django.shortcuts import render

# Create your views here.

class Authentications:
    def signin(request):
        return render(request, 'login.html')

class Home:
    def index(request):
        return render(request, 'index.html')