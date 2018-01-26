from django.urls import path

from . import views


app_name = 'projects'

urlpatterns = [
    # post views
    path('', views.project_list, name='project_list'),
    path('<slug:project_slug>/', views.project_detail, name='project_detail'),
    path('tag/<slug:tag_slug>/', views.project_list, name='project_list_by_tag'),
]