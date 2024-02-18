from apps.recipes.views import *
from django.urls import path

urlpatterns = [
    path("", view_home),
    path("contact/", view_contact),
    path("about/", view_about),
]






