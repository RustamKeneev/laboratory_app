from django.urls import path
from django.contrib.auth import views as auth_views

from rest.views import *

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('healthy-eating/', HealthyEatingView.as_view(), name='healthy_eating_list'),
    path('healthy-eating/<int:id>/', HealthyEatingDetailView.as_view(), name='healthy_eating_detail'),
    path('news/', NewsView.as_view(), name='news_list'),
    path('article/', ArticleView.as_view(), name='article_list'),
    path('news-article/detail/<int:id>/', NewsArticleDetailView.as_view(), name='news_article_detail'),
    path('med-center/', MedCenterView.as_view(), name='med_center_list'),
    path('laboratory/', LaboratoryView.as_view(), name='laboratory_list'),
    path('laboratory-med-center/detail/<int:id>/', LabMedDetailView.as_view(), name='lab_med_detail'),
    path('ajax/subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('confidentiality/', ConfidentialityView.as_view(), name='confidentiality')

]
