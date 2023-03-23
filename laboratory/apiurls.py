from django.urls import path
from laboratory.apiviews import *

urlpatterns = [
    path('categories/', CategoryAPI.as_view(), name='category_api'),
    path('categories/<int:category_id>/', AnalyzeSubcategoryAPI.as_view(), name='sub_category_api'),
]

