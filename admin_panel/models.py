from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SubMenu(models.Model):
    name = models.CharField(max_length=250)
    id_menu = models.ForeignKey(Menu,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name