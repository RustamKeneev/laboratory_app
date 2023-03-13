from django.urls import path
from laboratory.apiviews import *


path('category/', CategoryAPI.as_view(), name='category_api'),
