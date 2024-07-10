from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:topic>", views.page, name="page"),
    path("search/", views.search, name="search"),
]
