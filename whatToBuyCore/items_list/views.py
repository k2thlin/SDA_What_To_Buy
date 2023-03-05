from django.shortcuts import render, redirect
from .models import ShoppingList



# Create your views here.
def home(request):
    return render(request, "home.html")


def my_lists(request):
    if request.method == "GET":
        shopping_lists = ShoppingList.objects.filter(user=request.user)
        return render(request, "shopping_lists.html", context={"shopping_lists": shopping_lists})
    
    if request.method == "POST":
        if request.POST.get("recipe_add"):
            checked = False
            if request.POST.get("checkbox"):
                checked = True

            item_name = request.POST.get("recipe") 
            ShoppingList.objects.create(title = item_name, user = request.user, is_public=checked)
        elif request.POST.get("delete"):
            id_to_delete = request.POST.get("delete")
            item_to_delete = ShoppingList.objects.get(pk=id_to_delete)
            item_to_delete.delete()
        return redirect("lists-list")
    



def items_list(request, pk):
    shopping_list = ShoppingList.objects.get(pk=pk)
    items_list = shopping_list.shoppingitem_set.all()

    if request.method == "GET":
        return render(request, "shopping_list.html", context={"shopping_list": items_list, "header" : shopping_list})
    
    if request.method == "POST":
        if request.POST.get("item_add"):
            item_name = request.POST.get("item_name")
            item_description = request.POST.get("item_description")

            shopping_list.shoppingitem_set.create(name=item_name, description=item_description)

        elif request.POST.get("update_checked"):
            checked = request.POST.getlist("checkbox")
            for item in items_list:
                item.is_completed = True if str(item.pk) in checked else False
                item.save()
        elif request.POST.get("delete"):
            id_to_delete = request.POST.get("delete")
            item_to_delete = shopping_list.shoppingitem_set.get(pk=id_to_delete)
            item_to_delete.delete()

        return redirect("items-list", pk)
    

def public_list(request):
    public_lists = ShoppingList.objects.filter(is_public=True)
    return render(request, "public_list.html", context={"public_lists": public_lists})
