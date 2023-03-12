from django.http import JsonResponse
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Category, Lab, Analyze, PriceAnalyzeToLaboratory
from .serializers import CategorySerializer, AnalyzeSubcategorySerializer, LabSerializer, PriceAnalyzeToLaboratorySerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryList(generics.ListAPIView):
    serializer_class = AnalyzeSubcategorySerializer

    def get_queryset(self):
        return Analyze.objects.filter(parent_subcategory=None)


class CategoryDetail(APIView):

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


class SubcategoryDetail(RetrieveAPIView):
    queryset = Analyze.objects.all()
    serializer_class = AnalyzeSubcategorySerializer


class PriceAnalyzeToLaboratoryListView(ListAPIView):
    serializer_class = PriceAnalyzeToLaboratorySerializer
