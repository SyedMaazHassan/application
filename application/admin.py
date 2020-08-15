from django.contrib import admin
from .models import *

# Register your models here.

class available_item_admin(admin.ModelAdmin):
    list_display = ['id','category', 'sub_category', 'sub_sub_category', 'picture','item_name','price_per_unit', 'installed_vendor']
    list_editable = ['picture','item_name','category','price_per_unit', 'installed_vendor', 'sub_sub_category', 'sub_category']

    search_fields = ['item_name']

    ordering = ['id']



admin.site.register(categories)
admin.site.register(sub_categorie)
admin.site.register(sub_sub_categorie)
admin.site.register(available_item, available_item_admin)
