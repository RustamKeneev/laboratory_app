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


class DoctorListAPI(APIView):
    """Doctor list by DoctorType"""
    def get(self, request, **kwargs):
        doctors_list = Doctors.objects.filter(category_id=kwargs['doctorType_id'])
        data = DoctorListSerializer(doctors_list, many=True).data
        return Response(data)


class DoctorDetailAPI(APIView):
    """Doctor detail information"""
    def get(self, request, **kwargs):
        doctor = Doctors.objects.get(id=kwargs['doctor_id'])
        data = DoctorDetailSerializer(doctor).data
        return Response(data)
