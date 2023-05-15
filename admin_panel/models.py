from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


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
    
class SubmenuPost(TranslatableModel):
    translations = TranslatedFields (
        title = models.CharField(_('title'),max_length=250),
        content = RichTextUploadingField(_('content'),default=None,null=True,blank=True)
    )
    id_menu = models.ForeignKey(SubMenu,on_delete=models.CASCADE,null=True,blank=True)
    img = models.FileField(upload_to='posts',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = _("SubmenuPost")
        verbose_name_plural = _("SubmenuPosts")
    def __str__(self):
        return self.title


class Post(TranslatableModel):
    translations = TranslatedFields (
        title = models.CharField(_('title'),max_length=250),
        content = RichTextUploadingField(_('content'),default=None,null=True,blank=True)
    )
    img = models.FileField(upload_to='posts',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
    def __str__(self):
        return self.title



class Vacansy(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('title'),max_length=250),
        content = RichTextUploadingField(_('content'),default=None,null=True,blank=True)
    )
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = _("Vacansy")
        verbose_name_plural = _("Vacansys")
    def __str__(self):
        return self.title

    

