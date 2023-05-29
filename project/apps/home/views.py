from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, "home/index.html")

def laliga(request):
    now = datetime.now()
    Fecha = now.strftime("%d de  %B del %Y ")
    return render(request, "home/laliga.html", {"Fecha": Fecha})

def login(request):
    return render(request, "home/login.html")

def noticias(request):
    return render(request, "home/noticias.html")