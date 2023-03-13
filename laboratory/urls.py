from django.urls import path, include
from .views import  SubcategoryList, CategoryDetail, SubcategoryDetail, PriceAnalyzeToLaboratoryListView, \
    CategoryView
from .apiviews import *

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category'),
    path('subcategories/', SubcategoryList.as_view(), name='subcategory-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('subcategories/<int:pk>/', SubcategoryDetail.as_view(), name='subcategory-detail'),
    path('priceanalyze/', PriceAnalyzeToLaboratoryListView.as_view(), name='price-analyze'),
    path('category/', CategoryView.as_view(), name='category'),
]