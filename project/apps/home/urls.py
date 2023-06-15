from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   
    path("",views.index, name ="index"),
    path("laliga",views.laliga, name ="laliga"),
    path("login",views.login_request, name ="login"),
    path("registro",views.registro, name ="registro"),
    path("logout", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
    path("nosotros",views.nosotros, name ="nosotros"),
   
    

    # path("noticias",views.noticias, name ="noticias"),
]

urlpatterns += staticfiles_urlpatterns()

