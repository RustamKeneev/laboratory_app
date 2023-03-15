from django.urls import path
from rest.apiviews import *

urlpatterns = [
    path('news/', NewsAPI.as_view(), name='news_api'),
    path('article/', ArticleAPI.as_view(), name='article_api'),
    path('news-article/detail/<int:id>/', NewsArticleDetailAPI.as_view(), name='news_article_detail_api'),
    path('laboratory/', LaboratoryAPI.as_view(), name='laboratory_api'),
    path('lab-med/detail/<int:id>/', LabMedCenterDetailAPI.as_view(), name='lab_med_detail_api'),
    path('med-center/', MedCenterAPI.as_view(), name='med_center_api'),
    path('healthy-eating/', HealthyEatingAPI.as_view(), name='healthy_eating_api'),
    path('healthy-eating/detail/<int:healthy_eating_id>/', HealthyEatingDetailAPI.as_view(),
         name='healthy_eating_detail_api'),
    path('partner/', PartnerAPI.as_view(), name='partner_api'),
    path('slider/', SliderAPI.as_view(), name='slider_api'),
    path('banner/', BannerAPI.as_view(), name='banner_api'),

]
