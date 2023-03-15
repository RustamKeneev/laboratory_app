from rest_framework import serializers

from rest.models import *


class NewsAndArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsAndArticle
        fields = ['id', 'image', 'title', 'date', 'description', 'type']


class LaboratoryAndMedCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaboratoryAndMedCenter
        fields = ['id', 'image', 'title', 'address', 'date', 'description', 'type']


class HealthyEatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthyEating
        fields = ['id', 'image', 'title', 'date', 'description', ]


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'image', 'website', ]


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'image', 'website', ]


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'image', ]


