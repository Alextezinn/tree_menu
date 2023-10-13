from django.contrib import admin
from .models import MenuItem, Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ("title",)}


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ("title",)}


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
