from rest_framework.response import Response
from rest_framework.views import APIView
from rest.serializers import *


class NewsAPI(APIView):
    def get(self, request):
        news_list = NewsAndArticle.objects.filter(type='news')
        data = NewsAndArticleSerializer(news_list, many=True).data
        return Response(data)


class ArticleAPI(APIView):

    def get(self, request):
        article_list = NewsAndArticle.objects.filter(type='article')
        data = NewsAndArticleSerializer(article_list, many=True).data
        return Response(data)


class NewsArticleDetailAPI(APIView):
    def get(self, request, **kwargs):
        item = NewsAndArticle.objects.get(id=kwargs['id'])
        data = NewsAndArticleSerializer(item).data
        return Response(data)


class LaboratoryAPI(APIView):
    def get(self, request):
        laboratory_list = LaboratoryAndMedCenter.objects.filter(type='laboratory')
        data = LaboratoryAndMedCenterSerializer(laboratory_list, many=True).data
        return Response(data)


class MedCenterAPI(APIView):
    def get(self, request):
        med_center_list = LaboratoryAndMedCenter.objects.filter(type='med_center')
        data = LaboratoryAndMedCenterSerializer(med_center_list, many=True).data
        return Response(data)


class LabMedCenterDetailAPI(APIView):
    def get(self, request, **kwargs):
        item = LaboratoryAndMedCenter.objects.get(id=kwargs['id'])
        data = LaboratoryAndMedCenterSerializer(item).data
        return Response(data)


class HealthyEatingAPI(APIView):
    def get(self, request):
        healthy_eating_list = HealthyEating.objects.all()
        data = HealthyEatingSerializer(healthy_eating_list, many=True).data
        return Response(data)


class HealthyEatingDetailAPI(APIView):
    def get(self, request, **kwargs):
        healthy_eating = HealthyEating.objects.get(id=kwargs['healthy_eating_id'])
        data = HealthyEatingSerializer(healthy_eating).data
        return Response(data)


class PartnerAPI(APIView):
    def get(self, request):
        partner_list = Partner.objects.all()
        data = PartnerSerializer(partner_list, many=True).data
        return Response(data)


class SliderAPI(APIView):
    def get(self, request):
        slider_list = Slider.objects.all()
        data = SliderSerializer(slider_list, many=True).data
        return Response(data)


class BannerAPI(APIView):
    def get(self, request):
        banner_list = Banner.objects.all()
        data = BannerSerializer(banner_list, many=True).data
        return Response(data)


