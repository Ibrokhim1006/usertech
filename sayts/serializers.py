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