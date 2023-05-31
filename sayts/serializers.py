from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from admin_panel.models import *


class MenuSerializers(TranslatableModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','name','translations']
    def get_text(self, instance):
        return {
            'ru': instance.name_ru,
            'en': instance.name_en,
            'zh-hant':instance.name_zh_hant,
        }

class PostMenuSerizalizers(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=SubmenuPost)
    id_menu = MenuSerializers(read_only=True)
    class Meta:
        model = SubmenuPost
        fields = ['id','title','content','img','id_menu','translations']


class VacansySiteAllSerializers(TranslatableModelSerializer):
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

class VakansiyaPostSerizalizers(serializers.ModelSerializer):
    class Meta:
        model = VacansiyaPost
        fields = ['id','first_name','last_name','phone','e_mail','content','files','id_vacanys',]
    def create(self, validated_data):
        return VacansiyaPost.objects.create(**validated_data)



class Vakan(serializers.ModelSerializer):
    class Meta:
        model = VacansiyaPost
        fields = ['id','first_name','last_name','phone','e_mail','content','files','id_vacanys',]