from django import template

# from drug.models import Type, Drug
# from medical_device.models import Type as DeviceType
# from pharmacy.models import Region
# from rest.models import Contact, Banner

register = template.Library()

# @register.inclusion_tag('drug/region_list.html')
# def region_list():
#     regions = Region.objects.all()
#     return {'region_list': regions}