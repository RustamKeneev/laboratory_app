from django.urls import path
from laboratory.apiviews import *


path('category/', CategoryAPI.as_view(), name='category_api'),
path('subcategory/<int:category_id>/', AnalyzeSubcategoryAPI.as_view(), name='sub_category_api'),
