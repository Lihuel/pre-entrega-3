from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   
    path("",views.index, name ="index"),
    path("laliga",views.laliga, name ="laliga"),
    path("login/",LoginView.as_view(template_name="home/login.html"), name ="login"),
    path("registro",views.register, name ="register"),
    path("logout", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
    path("acerca_de_mi",views.acerca_de_mi, name ="acerca_de_mi"),
    path("admin",views.admin, name ="admin"),
   
    

    # path("noticias",views.noticias, name ="noticias"),
] + staticfiles_urlpatterns()

