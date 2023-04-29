from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from admin_panel.models import *


class UserSiginInSerizalizers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=250)
    class Meta:
        model = User
        fields = ['username','password',]


class UserPorfilesSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name',]


# Menu Serializers
class MenuAllSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','name',]

class MenuChangeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','name',]
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.save() 
        return instance

class SubMenuAllSeriazlizers(serializers.ModelSerializer):
    id_menu = MenuAllSerializers(read_only=True)
    class Meta:
        model = SubMenu
        fields = ['id','name','id_menu',]

class SubMenuAllSeriazlizerss(serializers.ModelSerializer):
    id_menu = MenuAllSerializers(read_only=True)
    class Meta:
        model = SubMenu
        fields = ['id','name','id_menu',]

class SubMenuCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubMenu
        fields = ['id','name','id_menu',]
    def create(self, validated_data):
        return SubMenu.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.id_menu = validated_data.get('id_menu',instance.id_menu)
        instance.save() 
        return instance