from django.shortcuts import render

def index(request):
    return render(request, "equipos/index.html")