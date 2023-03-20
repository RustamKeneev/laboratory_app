from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from doctors.serializers import *
from doctors.models import *


class DoctorTypeAPI(APIView):
    """All doctor type list"""
    def get(self, request):
        category_list = DoctorType.objects.all()
        data = DoctorTypeSerializer(category_list, many=True).data
        return Response(data)
