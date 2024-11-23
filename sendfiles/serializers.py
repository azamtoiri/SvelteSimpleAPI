from rest_framework import serializers

from pages.models import Component, PageComponent, Page


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ['id', 'name', 'type', 'schema']


class PageComponentSerializer(serializers.ModelSerializer):
    component = ComponentSerializer()

    class Meta:
        model = PageComponent
        fields = ['id', 'component', 'content', 'order']


class PageSerializer(serializers.ModelSerializer):
    components = PageComponentSerializer(source='pagecomponent_set', many=True)

    class Meta:
        model = Page
        fields = ['id', 'title', 'slug', 'layout', 'components']

