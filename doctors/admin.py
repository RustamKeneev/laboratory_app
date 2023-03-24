from django.contrib import admin
from doctors.models import Doctors, DoctorType, MedicalStaffPositions

admin.site.register(Doctors)
admin.site.register(DoctorType)
admin.site.register(MedicalStaffPositions)