from django.contrib import admin
from parler.admin import TranslatableAdmin
from import_export.admin import ImportExportActionModelAdmin,ImportExportModelAdmin
from admin_panel.models import *

@admin.register(Menu)
class CategoryAdmin(ImportExportModelAdmin,TranslatableAdmin):
    list_display = ['name']

@admin.register(SubMenu)
class SubMenuAdmin(TranslatableAdmin,ImportExportModelAdmin):
    list_display = ['name']

@admin.register(SubmenuPost)
class SubMenuPostsAdmin(TranslatableAdmin,ImportExportModelAdmin):
    list_display =['title']

@admin.register(Post)
class PostAdmin(TranslatableAdmin,ImportExportModelAdmin):
    list_display = ['title']