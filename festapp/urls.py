from django.urls import path
from .import views
urlpatterns=[
    path("",views.fest_home,name="fest_name"),
    path("about/",views.about,name="about"),
    path("collegefest/",views.collegefest,name="collegefest")


]