from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Food, SingletonModel , Shake ,Salat


from django.contrib import admin
from django.utils.html import format_html
from .models import Food

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image_preview')

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ['name', 'image_tag',]

    

@admin.register(SingletonModel)
class SingletonModelAdmin(admin.ModelAdmin):
    list_display = ('numbers',)

    def has_add_permission(self, request):
        # Prevent adding a new instance if one already exists
        return not SingletonModel.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False


@admin.register(Shake)
class ShakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image_preview')

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ['name', 'image_tag',]



@admin.register(Salat)
class Salat(admin.ModelAdmin):
    list_display = ('name', 'price', 'image_preview')

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ['name', 'image_tag',]
   
   


