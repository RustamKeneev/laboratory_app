from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Category, Lab, Analyze, PriceAnalyzeToLaboratory
from django.views.generic import TemplateView
from .serializers import CategorySerializer, AnalyzeSubcategorySerializer, LabSerializer, PriceAnalyzeToLaboratorySerializer
from rest.models import *


class SubcategoryList(generics.ListAPIView):
    serializer_class = AnalyzeSubcategorySerializer

    def get_queryset(self):
        return Analyze.objects.filter(parent_subcategory=None)


class CategoryDetail(TemplateView):
    model = Category
    template_name = 'laboratory/analyze_list.html'
    context_object_name = 'category'


class SubcategoryDetail(RetrieveAPIView):
    queryset = Analyze.objects.all()
    serializer_class = AnalyzeSubcategorySerializer


class PriceAnalyzeToLaboratoryListView(ListAPIView):
    serializer_class = PriceAnalyzeToLaboratorySerializer


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        slider_list = Slider.objects.all()
        partner_list = Partner.objects.all()
        healthy_eating = HealthyEating.objects.last()
        news = NewsAndArticle.objects.filter(type='news').last()
        contact = Contact.objects.last()
        return render(request, self.template_name, context={
            'slider_list': slider_list,
            'partner_list': partner_list,
            'healthy_eating': healthy_eating,
            'news': news,
            'contact': contact,
        })


class CategoryView(TemplateView):
    template_name = 'laboratory/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context

    # def get(self, request, *args, **kwargs):
    #     category_id = kwargs.get('category_id')
    #     if category_id:
    #         category = Category.objects.prefetch_related('subcategories').get(id=category_id)
    #         context = {'category': category}
    #     else:
    #         category_list = Category.objects.prefetch_related('subcategories').all()
    #         context = {'category_list': category_list}
    #     return render(request, self.template_name, context=context)


class CatalogView(TemplateView):
    template_name = 'laboratory/catalog.html'

    def get(self, request, *args, **kwargs):
        catalog_list = Category.objects.all()
        # catalog_list = Category.objects.prefetch_related('subcategories').all()
        return render(request, self.template_name, context={
            'catalog_list': catalog_list,
        })


class AnalyzeListView(TemplateView):
    template_name = 'laboratory/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_pk = self.kwargs['pk']
        subcategories = Analyze.objects.filter(category__pk=category_pk)
        context['subcategories'] = subcategories
        return context

    # def get(self, request, *args, **kwargs):
    #     # title = Analyze.objects.get(id=kwargs['category_id']).title
    #     # analyze_list = Analyze.objects.filter(category_id=kwargs['category_id'])
    #     analyze_list = Analyze.objects.all()
    #     return render(request, self.template_name, context={
    #         'analyze_list':analyze_list
    #         # 'title': title
    #     })


class PharmacyView(TemplateView):
    template_name = 'laboratory/pharmacy.html'

    def get(self, request, *args, **kwargs):
        pharmacy_list = Category.objects.all()
        return render(request, self.template_name, context={
            'pharmacy_list': pharmacy_list,
        })


class DoctorsView(TemplateView):
    template_name = 'laboratory/doctors.html'

    def get(self, request, *args, **kwargs):
        doctors_list = Category.objects.all()
        return render(request, self.template_name, context={
            'doctors_list': doctors_list,
        })


class NewsView(TemplateView):
    template_name = 'laboratory/news.html'

    def get(self, request, *args, **kwargs):
        news_list = Category.objects.all()
        return render(request, self.template_name, context={
            'news_list': news_list,
        })


class ArticlesView(TemplateView):
    template_name = 'laboratory/articles.html'

    def get(self, request, *args, **kwargs):
        articles_list = Category.objects.all()
        return render(request, self.template_name, context={
            'articles_list': articles_list,
        })


class ContactsView(TemplateView):
    template_name = 'laboratory/contacts.html'

    def get(self, request, *args, **kwargs):
        contacts_list = Category.objects.all()
        return render(request, self.template_name, context={
            'contacts_list': contacts_list,
        })