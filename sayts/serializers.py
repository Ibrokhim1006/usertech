from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from admin_panel.models import *


class MenuSerializers(TranslatableModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "name", "seo_h1", "ceo_content", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "zh-hant": instance.name_zh_hant,
        }


class PostMenuSerizalizers(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=SubmenuPost)
    id_menu = MenuSerializers(read_only=True)

    class Meta:
        model = SubmenuPost
        fields = [
            "id",
            "title",
            "content",
            "content_two",
            "img",
            "id_menu",
            "seo_h1",
            "ceo_content",
            "translations",
        ]


class VacansySiteAllSerializers(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Vacansy)

    class Meta:
        model = Vacansy
        fields = [
            "id",
            "title",
            "content",
            "date",
            "seo_h1",
            "ceo_content",
            "translations",
        ]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "zh-hant": instance.name_zh_hant,
        }


class VakansiyaPostSerizalizers(serializers.ModelSerializer):
    class Meta:
        model = VacansiyaPost
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone",
            "e_mail",
            "content",
            "files",
            "id_vacanys",
        ]

    def create(self, validated_data):
        return VacansiyaPost.objects.create(**validated_data)


class Vakan(serializers.ModelSerializer):
    class Meta:
        model = VacansiyaPost
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone",
            "e_mail",
            "content",
            "files",
            "id_vacanys",
        ]


class ApplicationSerializersPOst(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"

    def create(self, validated_data):
        return Application.objects.create(**validated_data)


class ComsultatsiyaSerializersPOst(serializers.ModelSerializer):
    class Meta:
        model = Consultatsiya
        fields = "__all__"

    def create(self, validated_data):
        return Consultatsiya.objects.create(**validated_data)


class FormaSerializersPOst(serializers.ModelSerializer):
    class Meta:
        model = Forma
        fields = "__all__"

    def create(self, validated_data):
        return Forma.objects.create(**validated_data)
