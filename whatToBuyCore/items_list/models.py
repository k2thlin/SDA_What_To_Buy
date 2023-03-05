from django.db.models import (CASCADE, CharField, ForeignKey,
 Model, TextField, BooleanField, DateField)
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.admin import ModelAdmin

# Create your models here.

class ItemsAdmin(ModelAdmin):

    @staticmethod
    def released_year(obj):
        return obj.released.year

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description=None)

    ordering = ['id']
    list_display = ['id', 'name','shopping_list', 'description', 'is_completed']
    list_display_links = ['id', 'name','description']
    list_per_page = 30
    list_filter = ['description']
    search_fields = ['name']
    actions = ['cleanup_description']
    fieldsets = [
        (None, {'fields': ['name']}),
        (
            'Link to Another table',
            {
                'fields': ['shopping_list'],
                'description': (
                    'Select form the list of possible lists.'
                )
            }
        ),
        (
            'Item Information',
            {
                'fields': ['description'],
                'description': 'These fields are intended to be filled in by our users.'
            }
        )
    ]
    readonly_fields = ['is_completed']



class ShoppingList(Model):
    title =  CharField("Shopping list name" , max_length=100 )
    user = ForeignKey(User,on_delete=CASCADE)
    greated_at = DateField(default= datetime.now())
    is_public = BooleanField(default=False)

    def __str__(self):
        return self.title



class ShoppingItem(Model):
    name= CharField("Shopping list item name", max_length=100)
    description = CharField("Shoppin list item description", max_length=300, null=True, blank=True)
    is_completed = BooleanField(default=False)
    shopping_list = ForeignKey(ShoppingList, on_delete=CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('items-list', kwargs={'pk': self.shopping_list.pk})
