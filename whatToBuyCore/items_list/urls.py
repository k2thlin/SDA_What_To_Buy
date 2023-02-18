from django.urls import path
from .views import my_lists, items_list

urlpatterns = [
    path("my_lists/", my_lists, name="lists-list"),
    path("my_lists/<pk>/", items_list, name= "items-list"),
]

