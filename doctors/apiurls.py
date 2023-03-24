from django.urls import path
from doctors.apiviews import *

urlpatterns = [
    path('doctor_types_api/', DoctorTypeAPI.as_view(), name='doctor_type_api'),
    path('doctor_types_api/<int:doctorType_id>/', DoctorListAPI.as_view(), name='doctor_list_api'),
    path('doctor_types_api/<int:doctorType_id>/<int:pk>', DoctorDetailAPI.as_view(), name='doctor_detail_api'),
]