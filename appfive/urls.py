from django.urls import path
from . import views

#Template name
app_name = "appfive"

urlpatterns = [
    path('register/',views.register , name="register"),
    path("login/",views.user_login,name="login"),
    path("logout/",views.user_logout,name="logout"),
    path("special/",views.special_page,name="special")
]