from django import template
from doctors.models import *
from laboratory.templatetags.laboratory_tags import register
from rest.models import *


@register.inclusion_tag('rest/side_bar.html')
def side_bar():
    banner_list = Banner.objects.order_by('?')[0:2]
    return {'banner_list': banner_list}
