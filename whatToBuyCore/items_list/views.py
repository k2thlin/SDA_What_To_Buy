from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView



# Create your views here.


def my_lists(request):
    shopping_lists = ShoppingList.objects.all()
    return render(request, "shopping_lists.html", context={"shopping_lists": shopping_lists})

def items_list(request, pk):
    shopping_list = ShoppingList.objects.get(pk=pk)
    items_list = shopping_list.shoppingitem_set.all()
    return render(request, "shopping_list.html", context={"shopping_list": items_list})