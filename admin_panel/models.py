from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Menu(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("name"), max_length=250),
        content=RichTextUploadingField(
            _("content"), default=None, null=True, blank=True
        ),
    )
    seo_h1 = models.CharField(max_length=250, null=True, blank=True)
    ceo_content = models.TextField(null=True, blank=True)
    img = models.CharField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]
        verbose_name = _("Menu")
        verbose_name_plural = _("Menu")

    def __str__(self):
        return self.name


class SubmenuPost(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("title"), max_length=250),
        content=RichTextUploadingField(
            _("content"), default=None, null=True, blank=True
        ),
        content_two=RichTextUploadingField(
            _("content"), default=None, null=True, blank=True
        ),
    )
    seo_h1 = models.CharField(max_length=250, null=True, blank=True)
    ceo_content = models.TextField(null=True, blank=True)
    id_menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True)
    img = models.CharField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]
        verbose_name = _("SubmenuPost")
        verbose_name_plural = _("SubmenuPosts")

    def __str__(self):
        return self.title


class Post(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("title"), max_length=250),
        content=RichTextUploadingField(
            _("content"), default=None, null=True, blank=True
        ),
    )
    seo_h1 = models.CharField(max_length=250, null=True, blank=True)
    ceo_content = models.TextField(null=True, blank=True)
    img = models.CharField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")


class Vacansy(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("title"), max_length=250),
        content=RichTextUploadingField(
            _("content"), default=None, null=True, blank=True
        ),
    )
    seo_h1 = models.CharField(max_length=250, null=True, blank=True)
    ceo_content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]
        verbose_name = _("Vacansy")
        verbose_name_plural = _("Vacansys")

    def __str__(self):
        return self.title


class VacansiyaPost(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    e_mail = models.CharField(max_length=250)
    content = models.TextField()
    files = models.FileField(upload_to="doc/", null=True, blank=True)
    id_vacanys = models.ForeignKey(
        Vacansy, on_delete=models.CASCADE, null=True, blank=True
    )
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Application(models.Model):
    full_name = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Consultatsiya(models.Model):
    full_name = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Forma(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    companiya = models.CharField(max_length=250)
    about = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name + "" + self.last_name
