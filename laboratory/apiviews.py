from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from laboratory.serializers import *
from laboratory.models import *


class CategoryAPI(APIView):
    """All category list"""
    @staticmethod
    def get(request):
        category_list = Category.objects.all()
        data = CategorySerializer(category_list, many=True).data
        return Response(data)


class AnalyzeSubcategoryAPI(APIView):
    """Analyze subcategory list by category"""
    def get(self, request, **kwargs):
        analyze_sub_category_list = Analyze.objects.filter(category_id=kwargs['category_id'])
        data = SubcategorySerializer(analyze_sub_category_list, many=True).data
        return Response(data)


class AnalyzeDetailAPI(APIView):
    """Analyze detail information"""
    def get(self, request, **kwargs):
        analyze = Analyze.objects.get(id=kwargs['analyze_id'])
        data = AnalyzeSubcategorySerializer(analyze).data
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


class LaboratoryDetailAPI(APIView):
    """Laboratory detail information"""
    def get(self, request, **kwargs):
        laboratory = Lab.objects.get(id=kwargs['laboratory_id'])
        data = LabSerializer(laboratory).data
        return Response(data)






