from django.contrib import admin
from parler.admin import TranslatableAdmin

from admin_panel.models import *

@admin.register(Menu)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name']

@admin.register(SubMenu)
class SubMenuAdmin(TranslatableAdmin):
    list_display = ['name','id_menu']
