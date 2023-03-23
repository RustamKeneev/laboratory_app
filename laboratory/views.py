from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from .models import Category, Lab, Analyze
from django.views.generic import TemplateView
from .serializers import AnalyzeSubcategorySerializer
from rest.models import *


class SubcategoryList(generics.ListAPIView):
    serializer_class = AnalyzeSubcategorySerializer

    def get_queryset(self):
        return Analyze.objects.filter(parent_subcategory=None)


class CategoryDetail(TemplateView):
    model = Category
    template_name = 'laboratory/analyze_list.html'
    context_object_name = 'category'


# class SubcategoryDetail(RetrieveAPIView):
#     queryset = Analyze.objects.all()
#     serializer_class = AnalyzeSubcategorySerializer


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


class CatalogView(TemplateView):
    template_name = 'laboratory/catalog.html'

    def get(self, request, *args, **kwargs):
        catalog_list = Category.objects.all()
        return render(request, self.template_name, context={
            'catalog_list': catalog_list,
        })


class AnalyzeListView(TemplateView):
    template_name = 'laboratory/analyze_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_pk = self.kwargs['pk']
        subcategories = Analyze.objects.filter(category__pk=category_pk)
        context['subcategories'] = subcategories
        return context


class AnalyzeDetailView(TemplateView):
    template_name = 'laboratory/analyze_detail.html'

    def get(self, request, *args, **kwargs):
        analyze = Analyze.objects.get(id=kwargs['id'])
        return render(request, self.template_name, context={
            'analyze': analyze,
        })


class LaboratoryListView(TemplateView):
    template_name = 'laboratory/laboratory_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['laboratories'] = Lab.objects.all()
        return context


class LaboratoryDetailView(TemplateView):
    template_name = 'laboratory/laboratory_detail.html'

    def get(self, request, *args, **kwargs):
        laboratory_detail = Lab.objects.get(id=kwargs['id'])
        return render(request, self.template_name, context={
            'laboratory_detail': laboratory_detail,
        })


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