from django.shortcuts import render
from django.http import HttpResponse
from .models import ShoppingList, ShoppingItem
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

class ItemCreateView(CreateView):
    model = ShoppingItem
    fields = '__all__'

class ItemUpdateView(UpdateView):
    model = ShoppingItem
    fields = '__all__'

class ItemDeleteView(DeleteView):
    model = ShoppingItem
    success_url = reverse_lazy("items_list")


def my_lists(request):
    shopping_lists = ShoppingList.objects.all()
    return render(request, "shopping_lists.html", context={"shopping_lists": shopping_lists})

def items_list(request, pk):
    shopping_list = ShoppingList.objects.get(pk=pk)
    items_list = shopping_list.shoppingitem_set.all()
    return render(request, "shopping_list.html", context={"shopping_list": items_list})