from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from admin_panel.mixins import *
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


#===================================Menu Serializers============================
class SubMenuAllSeriazlizers(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Menu)
    class Meta:
        model = Menu
        fields = ['id','name','content','img','translations']
    def get_text(self, instance):
        return {
            'ru': instance.name_ru,
            'en': instance.name_en,
            'zh-hant':instance.name_zh_hant,
        }
class SubMenuAllSeriazlizerss(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Menu)
    class Meta:
        model = Menu
        fields = ['id','name','content','img','translations']
class SubMenuCRUDSerializers(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Menu)
    class Meta:
        model = Menu
        fields = ['id','name','content','img','translations']
    def get_text(self, instance):
        return {
            'ru': instance.name_ru,
            'en': instance.name_en,
            'zh-hant':instance.name_zh_hant,
        }
    def create(self, validated_data):
        return Menu.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.content = validated_data.get('content',instance.content)
        instance.img = validated_data.get('img',instance.img)
        instance.save() 
        return instance

#==================================SubMenu Posts Serializers=======================================
class SubMenuPostSeriazlizers(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=SubmenuPost)
    id_menu = SubMenuAllSeriazlizers(read_only=True)
    class Meta:
        model = SubmenuPost
        fields = ['id','title','content','content_two','img','id_menu','translations']

class SubMenuPostCRUDSerializers(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=SubmenuPost)
    class Meta:
        model = SubmenuPost
        fields = ['id','title','content','content_two','img','id_menu','translations']
    def get_text(self, instance):
        return {
            'ru': instance.name_ru,
            'en': instance.name_en,
            'zh-hant':instance.name_zh_hant,
        }
    def create(self, validated_data):
        return SubmenuPost.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.content = validated_data.get('content',instance.content)
        instance.content_two = validated_data.get('content_two',instance.content_two)
        instance.id_menu = validated_data.get('id_menu',instance.id_menu)
        instance.img = validated_data.get('img',instance.img)
        instance.save() 
        return instance

#==================================Posts Serializers=======================================
class PostBaseAllSerializers(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Post)
    class Meta:
        model = Post
        fields = ['id','title','content','img','date','translations']
    def get_text(self, instance):
        return {
            'ru': instance.name_ru,
            'en': instance.name_en,
            'zh-hant':instance.name_zh_hant,
        }
class PostBaseCrudSerializers(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Post)
    class Meta:
        model = Post
        fields = ['id','title','content','img','date','translations']
    def get_text(self, instance):
        return {
            'ru': instance.name_ru,
            'en': instance.name_en,
            'zh-hant':instance.name_zh_hant,
        }
    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.content = validated_data.get('content',instance.content)
        instance.img = validated_data.get('img',instance.img)
        instance.save() 
        return instance
    
#==================================Vacansy Serializers=======================================

class VacansyBaseAllSerializers(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Vacansy)
    class Meta:
        model = Vacansy
        fields = ['id','title','content','date','translations']
    def get_text(self, instance):
        return {
            'ru': instance.name_ru,
            'en': instance.name_en,
            'zh-hant':instance.name_zh_hant,
        }
class VacanysBaseCrudSerializers(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Vacansy)
    class Meta:
        model = Vacansy
        fields = ['id','title','content','date','translations']
    def get_text(self, instance):
        return {
            'ru': instance.name_ru,
            'en': instance.name_en,
            'zh-hant':instance.name_zh_hant,
        }
    def create(self, validated_data):
        return Vacansy.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.content = validated_data.get('content',instance.content)
        instance.save() 
        return instance
#==================Forma serizliaers=======================
class ApplicationSerizliers(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
class ConsultatsiyaSerizliers(serializers.ModelSerializer):
    class Meta:
        model = Consultatsiya
        fields = '__all__'
class FormaSerizliers(serializers.ModelSerializer):
    class Meta:
        model = Forma
        fields = '__all__'