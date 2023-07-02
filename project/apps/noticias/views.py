from django.shortcuts import render, redirect
from . import forms



def index(request):
    return render(request, "noticias/index.html")

def crearnoticia(request):
   if request.method == "POST":
      form = forms.NoticiaForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("noticias:index")
   form = forms.NoticiaForm()
   context = {'form': form}
   return render(request, "noticias/crearnoticia.html", context)
   