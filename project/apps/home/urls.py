from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   
    path("",views.index, name ="index"),
    path("laliga",views.laliga, name ="laliga"),
    path("login",views.login, name ="login"),
    path("noticias",views.noticias, name ="noticias"),
]

urlpatterns += staticfiles_urlpatterns()

