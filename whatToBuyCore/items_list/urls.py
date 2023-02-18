from django.urls import path
from .views import my_lists, items_list, ItemCreateView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path("my_lists/", my_lists, name="lists-list"),
    path("my_lists/<pk>/", items_list, name= "items-list"),
    path("item/add/", ItemCreateView.as_view(), name= "item-add"),
    path("item/<int:pk>/update/", ItemUpdateView.as_view(), name= "item-update"),
    path("item/<int:pk>/delete/", ItemDeleteView.as_view(), name= "item-delete")
]

