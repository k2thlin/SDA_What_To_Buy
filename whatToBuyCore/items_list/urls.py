from django.urls import path
from . import views

urlpatterns = [
    path("my_lists/", views.my_lists),
    path("my_lists/<id>", views.items_list),
]
