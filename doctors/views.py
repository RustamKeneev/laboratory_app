from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class DoctorTypeView(TemplateView):
    template_name = 'doctors/doctor_type_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctor_types = DoctorType.objects.all()
        context['doctor_types'] = doctor_types
        return context


class DoctorListView(TemplateView):
    template_name = 'doctors/doctor_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctors_pk = self.kwargs['pk']
        doctors = Doctors.objects.filter(doctorType__pk=doctors_pk)
        context['doctorType'] = doctors
        return context


class DoctorDetailView(TemplateView):
    template_name = 'doctors/doctor_detail.html'

    def get(self, request, *args, **kwargs):
        doctors = Doctors.objects.get(id=kwargs['id'])
        return render(request, self.template_name, context={
            'doctors': doctors,
        })