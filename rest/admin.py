from django.contrib import admin

from rest.models import *


class NewsAndArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_tag', 'title', 'type', ]
    list_display_links = list_display
    search_fields = ['title', ]
    readonly_fields = ['image_tag_normal']
    list_filter = ['type']


class LaboratoryAndMedCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_tag', 'title', 'type', ]
    list_display_links = list_display
    search_fields = ['title', ]
    readonly_fields = ['image_tag_normal']
    list_filter = ['type']


class HealthyEatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_tag', 'title', ]
    list_display_links = list_display
    search_fields = ['title', ]
    readonly_fields = ['image_tag_normal']


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_tag', 'website', ]
    list_display_links = list_display
    search_fields = ['website', ]
    readonly_fields = ['image_tag_normal']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_tag', 'website', ]
    list_display_links = list_display
    search_fields = ['website', ]
    readonly_fields = ['image_tag_normal']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_tag', ]
    list_display_links = list_display
    readonly_fields = ['image_tag_normal']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email', ]
    list_display_links = list_display

    def has_add_permission(self, request):
        return self.model.objects.count() < 1


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['email', 'date']
    list_display_links = None

    def has_add_permission(self, request):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    # def has_change_permission(self, request, obj=None):
    #     return False


class ConfidentialityAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        obj_count = self.model.objects.count()
        if obj_count > 0:
            return False
        return super(ConfidentialityAdmin, self).has_add_permission(request)


admin.site.register(NewsAndArticle, NewsAndArticleAdmin)
admin.site.register(LaboratoryAndMedCenter, LaboratoryAndMedCenterAdmin)
admin.site.register(HealthyEating, HealthyEatingAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(Confidentiality, ConfidentialityAdmin)
