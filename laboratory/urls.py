from django.urls import path, include
from .views import *
from .apiviews import *

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('pharmacy/', PharmacyView.as_view(), name='pharmacy'),
    path('doctors/', DoctorsView.as_view(), name='doctors'),
    path('news/', NewsView.as_view(), name='news'),
    path('articles/', ArticlesView.as_view(), name='articles'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('subcategories/', SubcategoryList.as_view(), name='subcategory-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('subcategories/<int:pk>/', SubcategoryDetail.as_view(), name='subcategory-detail'),
    path('priceanalyze/', PriceAnalyzeToLaboratoryListView.as_view(), name='price-analyze'),
    path('category/', CategoryView.as_view(), name='category'),
]