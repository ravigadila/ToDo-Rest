from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'list/create/$', views.CreateList.as_view(), name='list_create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
