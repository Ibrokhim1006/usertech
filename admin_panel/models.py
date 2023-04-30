from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields

class Menu(TranslatableModel):
    translations = TranslatedFields (
        name = models.CharField(_('name'),max_length=250)
    ) 
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date']
        verbose_name = _("Menu")
        verbose_name_plural = _("Menus")
    def __str__(self):
        return self.name

class SubMenu(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('name'),max_length=250)
    )
    id_menu = models.ForeignKey(Menu,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date']
        verbose_name = _("SubMenu")
        verbose_name_plural = _("SubMenus")
    def __str__(self):
        return self.name