from django.urls import path
from . import views


urlpatterns = [
    path("", views.hello, name="hello"),
    path("gang", views.gang),
    path("emobilis", views.emobilis),
    path("home", views.home, name="home"),


]
