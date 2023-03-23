from django.contrib import admin
from .models import Category, Lab, Analyze, PriceAnalyzeToLaboratory


class PriceAnalyzeToLaboratoryAdmin(admin.TabularInline):
    model = PriceAnalyzeToLaboratory
    extra = 0
    fields = ("laboratory", "price")


@admin.register(Analyze)
class LaboratoryAdmin(admin.ModelAdmin):
    inlines = [PriceAnalyzeToLaboratoryAdmin]


admin.site.register(Category)
admin.site.register(Lab)
