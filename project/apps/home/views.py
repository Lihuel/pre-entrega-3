from django.shortcuts import render
from datetime import datetime
from . import forms


def index(request):
    return render(request, "home/index.html")

def laliga(request):
    now = datetime.now()
    # Fecha = now.strftime("%d de  %B del %Y ")
    fecha = f"{now}".split()[0] 
    year,month,day = fecha.split("-") 
    months = {1:"Enero", 2: "Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto"}
    Fecha = f"{day} de {months[int(month)]} del {year}"
    return render(request, "home/laliga.html", {"Fecha": Fecha})


def acerca_de_mi(request):
    return render(request, "home/acerca_de_mi.html")


def register(request):
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "home/index.html", {"Usuario": username})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "home/register.html", {"form": form})

def admin(request):
    return render(request, "home/admin.html")
