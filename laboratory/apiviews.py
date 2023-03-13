from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from laboratory.serializers import *
from laboratory.models import Category


# class CategoryAPI(APIView):
#     """All category list"""
#     def get(self, request):
#         category_list = Category.objects.all()
#         data = CategorySerializer(category_list, many=True).data
#         return Response(data)


class CategoryAPI(generics.ListAPIView):
    """All category list"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
