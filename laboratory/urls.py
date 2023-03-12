from django.urls import path, include
from .views import CategoryList, SubcategoryList, CategoryDetail, SubcategoryDetail, PriceAnalyzeToLaboratoryListView


urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('subcategories/', SubcategoryList.as_view(), name='subcategory-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('subcategories/<int:pk>/', SubcategoryDetail.as_view(), name='subcategory-detail'),
    path('priceanalyze/', PriceAnalyzeToLaboratoryListView.as_view(), name='price-analyze'),
]