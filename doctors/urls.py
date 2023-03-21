from django.urls import path, include
from .views import *
from .apiviews import *

urlpatterns = [
    path('doctortypes/', DoctorTypeView.as_view(), name='doctor_type'),
    path('doctors/<int:pk>/', DoctorListView.as_view(), name='doctor_list'),
    path('doctordetail/<int:id>/', DoctorDetailView.as_view(), name='doctor_detail'),
]