"""laboratory_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from laboratory import views
from laboratory_app import settings
from rest_framework_swagger.views import get_swagger_view
# from django.conf.urls import url
from django.conf.urls import ( handler400, handler403, handler404, handler500)

# handler400 = 'my_app.views.bad_request'
# handler403 = 'my_app.views.permission_denied'
# handler404 = 'my_app.views.page_not_found'
# handler500 = 'my_app.views.server_error'

schema_view = get_swagger_view(title='Online Pharmacy API')


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^api-token-auth/', rf_views.obtain_auth_token),
    path('api/', schema_view),
    # url(r'^$', schema_view),
    path('api/v1/', include("laboratory.urls")),
    path('api/v1/', include("doctors.urls")),
    path('', views.IndexView.as_view(), name='index'),
    path('laboratory/api/', include('laboratory.apiurls')),
    # path('laboratory/api/', include('laboratory.apiurls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)