from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from rest.models import *


class HealthyEatingView(TemplateView):
    template_name = 'rest/healthy_eating_list.html'

    def get(self, request, *args, **kwargs):
        healthy_eating_list = HealthyEating.objects.all()
        return render(request, self.template_name, context={
            'healthy_eating_list': healthy_eating_list,
        })


class HealthyEatingDetailView(TemplateView):
    template_name = 'rest/news_article_h_eating_detail.html'

    def get(self, request, *args, **kwargs):
        item = HealthyEating.objects.get(id=kwargs['id'])
        return render(request, self.template_name, context={
            'item': item,
        })


class NewsView(TemplateView):
    template_name = 'rest/news_list.html'

    def get(self, request, *args, **kwargs):
        print(request.user)
        news_list = NewsAndArticle.objects.filter(type='news')
        return render(request, self.template_name, context={
            'news_list': news_list,
        })


class ArticleView(TemplateView):
    template_name = 'rest/article_list.html'

    def get(self, request, *args, **kwargs):
        print(request.user)
        article_list = NewsAndArticle.objects.filter(type='article')
        return render(request, self.template_name, context={
            'article_list': article_list,
        })


class NewsArticleDetailView(TemplateView):
    template_name = 'rest/news_article_h_eating_detail.html'

    def get(self, request, *args, **kwargs):
        item = NewsAndArticle.objects.get(id=kwargs['id'])
        return render(request, self.template_name, context={
            'item': item,
        })


class MedCenterView(TemplateView):
    template_name = 'rest/med_center_list.html'

    def get(self, request, *args, **kwargs):
        med_center_list = LaboratoryAndMedCenter.objects.filter(type='med_center')
        return render(request, self.template_name, context={
            'med_center_list': med_center_list,
        })


class LaboratoryView(TemplateView):
    template_name = 'rest/laboratory_list.html'

    def get(self, request, *args, **kwargs):
        laboratory_list = LaboratoryAndMedCenter.objects.filter(type='laboratory')
        return render(request, self.template_name, context={
            'laboratory_list': laboratory_list,
        })


class LabMedDetailView(TemplateView):
    template_name = 'rest/lab_med_detail.html'

    def get(self, request, *args, **kwargs):
        item = LaboratoryAndMedCenter.objects.get(id=kwargs['id'])
        return render(request, self.template_name, context={
            'item': item,
        })


class AboutView(TemplateView):
    template_name = 'rest/about.html'

    def get(self, request, *args, **kwargs):
        about = Contact.objects.first().about
        return render(request, self.template_name, context={
            'about': about,
        })


class SubscribeView(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            Subscribe.objects.create(email=request.GET['email'])
        except:
            return HttpResponse('not_ok')
        return HttpResponse('ok')


class ConfidentialityView(TemplateView):
    template_name = 'rest/confidentiality.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['confidentiality'] = Confidentiality.objects.first()

        return context