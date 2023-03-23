from django.urls import path
from laboratory.apiviews import *

urlpatterns = [
    path('categories/', CategoryAPI.as_view(), name='category_api'),
    path('categories/<int:category_id>/', AnalyzeSubcategoryAPI.as_view(), name='sub_category_api'),
    path('categories/<int:category_id>/<int:analyze_id>', AnalyzeDetailAPI.as_view(), name='analyze_detail_api'),
    path('laboratories/', LaboratoryListAPI.as_view(), name='laboratory_list__api'),
    path('laboratories/<int:laboratory_id>/', LaboratoryDetailAPI.as_view(), name='laboratory_api'),
]
