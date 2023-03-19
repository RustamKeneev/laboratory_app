from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from laboratory.serializers import *
from laboratory.models import Category


class CategoryAPI(APIView):
    """All category list"""
    def get(self, request):
        category_list = Category.objects.all()
        data = CategorySerializer(category_list, many=True).data
        return Response(data)


class AnalyzeSubcategoryAPI(APIView):
    """Analyze subcategory list by category"""
    def get(self, request, **kwargs):
        analyze_sub_category_list = Analyze.objects.filter(category_id=kwargs['category_id'])
        data = SubcategorySerializer(analyze_sub_category_list, many=True).data
        return Response(data)


class CategoryDetailAPI(APIView):

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LaboratoryListAPI(APIView):
    """All laboratory list"""
    def get(self, request):
        laboratory_list = Lab.objects.all()
        data = LabSerializer(laboratory_list, many=True).data
        return Response(data)