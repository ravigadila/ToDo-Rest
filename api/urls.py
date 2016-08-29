from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'list/create/$', views.CreateList.as_view(), name='list_create'),
    url(r'list/edit/(?P<pk>[0-9]+)/$', views.EditList.as_view(), name='list_edit'),
    url(r'list/all/$', views.AllLists.as_view(), name='list_all'),
    url(r'item/create/$', views.CreateItem.as_view(), name='item_create'),
    url(r'item/edit/(?P<pk>[0-9]+)/$', views.EditItem.as_view(), name='item_edit'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
