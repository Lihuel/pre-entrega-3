from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, "home/index.html")

def laliga(request):
    fecha = datetime.now()
    return render(request, "home/laliga.html")

def login(request):
    return render(request, "home/login.html")

def noticias(request):
    return render(request, "home/noticias.html")