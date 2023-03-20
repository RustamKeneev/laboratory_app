from django.urls import path, include
from .views import *
from .apiviews import *

urlpatterns = [
    path('doctortypes/', DoctorTypeView.as_view(), name='doctor_type'),
    # path('category/<int:pk>/', AnalyzeListView.as_view(), name='sub-category-list'),
]