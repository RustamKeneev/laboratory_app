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


class CategoryDetail(APIView):

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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

    def get(self, request, *args, **kwargs):
        category_list = Category.objects.all()
        return render(request, self.template_name, context={
            'category_list': category_list,
        })


class CatalogView(TemplateView):
    template_name = 'laboratory/catalog.html'

    def get(self, request, *args, **kwargs):
        catalog_list = Category.objects.all()
        return render(request, self.template_name, context={
            'catalog_list': catalog_list,
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