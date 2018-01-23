from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag

# Create your views here.
from .models import Project

def project_list(request, tag_slug=None):
    object_list = Project.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        projects = paginator.page(paginator.num_pages)

    return render(request,
                  'projects/project/list.html',
                  {'page': page,
                   'projects': projects,
                   'tag': tag})


def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug, status='published')
    return render(request,
                  'projects/project/detail.html',
                  {'project': project})


