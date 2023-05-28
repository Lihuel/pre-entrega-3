from django.shortcuts import render

def index(request):
    return render(request, "home/index.html")

def laliga(request):
    return render(request, "home/laliga.html")

def login(request):
    return render(request, "home/login.html")

def noticias(request):
    return render(request, "home/noticias.html")