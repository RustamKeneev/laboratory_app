"""laboratory_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from laboratory.views import CategoryDetail, SubcategoryAnalyze,
# from laboratory.views import SubcategoryDetailView
# from laboratory.views import CategoryViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("laboratory.urls")),
    # path('api/v1/categories/', CategoryViewSet.as_view(), name="subcategories")
    # path('api/v1/analyze_subcategories/', SubcategoryAnalyze.as_view(), name="analyze_subcategories"),
    # path('categories/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    # path('subcategories/<int:id>/', SubcategoryDetailView.as_view(), name='subcategory_detail'),

]
