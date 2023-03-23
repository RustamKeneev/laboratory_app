from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category'),
    path('category/<int:pk>/', AnalyzeListView.as_view(), name='sub-category-list'),
    path('analyzedetail/<int:id>/', AnalyzeDetailView.as_view(), name='analyze-detail'),
    path('laboratories/', LaboratoryListView.as_view(), name='laboratory_list'),
    path('laboratories/<int:id>', LaboratoryDetailView.as_view(), name='laboratory_detail'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('pharmacy/', PharmacyView.as_view(), name='pharmacy'),
    path('doctors/', DoctorsView.as_view(), name='doctors'),
    path('news/', NewsView.as_view(), name='news'),
    path('articles/', ArticlesView.as_view(), name='articles'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('subcategories/', SubcategoryList.as_view(), name='subcategory-list'),
]
