from rest_framework import serializers
from .models import Category, Lab, Analyze, PriceAnalyzeToLaboratory


class PriceAnalyzeToLaboratorySerializer(serializers.ModelSerializer):
    lab_name = serializers.CharField(source='laboratory.name')
    lab_image = serializers.ImageField(source='laboratory.image')

    class Meta:
        model = PriceAnalyzeToLaboratory
        fields = ("lab_name", "price", "lab_image")


class LabSerializer(serializers.ModelSerializer):
    prices = PriceAnalyzeToLaboratorySerializer(many=True, source='prices_lab')

    class Meta:
        model = Lab
        fields = ('id', 'name', 'description', 'image', 'latitude', 'longitude', 'phone', 'address',
                  'website', 'date', 'prices')


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Analyze
        fields = ['id', 'title', 'category']


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategories']


class AnalyzeSubcategorySerializer(serializers.ModelSerializer):
    lab_prices = PriceAnalyzeToLaboratorySerializer(read_only=True, many=True)

    class Meta:
        model = Analyze
        fields = ('id', 'title', 'description', 'preparationForAnalysis', 'requirements', 'interpretationOfResults',
                  'laboratoryTest', 'biomaterial', 'deadlineDateOfIssueOfResults', 'category', 'parent_subcategory',
                  'lab_prices')
