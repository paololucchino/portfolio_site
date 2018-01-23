from django.conf.urls import url

from . import views

urlpatterns = [
    # post views
    url(r'^$', views.project_list, name='project_list'),
    url(r'^(?P<project_slug>[-\w]+)/$',
        views.project_detail,
        name='project_detail'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.project_list,
        name='project_list_by_tag'),
]