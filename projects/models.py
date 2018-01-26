from django.db import models
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.


'''
+++
publication = "PEDL Research Papers"
abstract="This paper by provides evidence about whether access to light, which relaxes the time constraint in relation to the number of productive hours available, can stimulate the emergence of currently pent-up productive potential, particularly of women. In doing so, it also brings evidence to the broader question of whether a cheap and renewable source of energy used exclusively for lighting, like a solar lamp, allows to reap (some of) the above economic benefits of full scale electrification. To understand and quantify these dynamics, we exploit random variation in solar lamp ownership among 806 parents participating in the companion randomised controlled trail on the effects of access to light on education. The authors find that access to light contributes to a diversification in household livelihoods from agricultural to non-farm economic activities. This evidence is supported by a consistent set of results across time use, the incidence of different productive activities, and incomes levels. To the authors' knowledge, this constitutes the first robust evidence that small scale lighting source can help stimulate the very first steps in the direction of economic transformation. At the same time, the paper delivers some sobering evidence on the gender dimension of the effect of access to light. While we find evidence that access to light does indeed relax time constraints, and those of women in particular, we find that a large part of the benefits of this additional time ultimately flows to men."
image_preview = ""
publication_short = ""
url_pdf = "http://pedl.cepr.org/sites/default/files/Female%20entrepreneurship%20and%20the%20role%20of%20access%20to%20light_working%20paper_0.pdf"
title = "Entrepreneurship, gender and the constraints of time: a randomised experiment on the role of access to light"
url_code = ""
url_video = ""
url_slides = ""
selected = false
authors = ["Fadi Hassan","Paolo Lucchino"]
url_dataset = ""
publication_types = ["3"]
url_project = ""
abstract_short = ""
date = "2017-09-01T21:53:36+02:00"
highlight = true
math = false

[header]
  caption = ""
  image = ""

+++


'''

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


def build_timestamped_filename(instance, filename):
    import os
    filename_base, filename_ext = os.path.splitext(filename)
    return '%s%s%s' % (
        timezone.now().strftime("%Y%m%d%H%M%S"),
        filename_base,
        filename_ext.lower(),
    )


class Project(models.Model):
    STATUS_CHOICES = (
       ('draft', 'Draft'),
       ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='start_date')
    body = models.TextField()
    image = models.ImageField(upload_to=build_timestamped_filename, blank=True)

    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    code_url = models.URLField(max_length=250, blank=True)
    publication_url = models.URLField(max_length=250, blank=True)
    external_url = models.URLField(max_length=250, blank=True)

    status = models.CharField(max_length=10,
                             choices=STATUS_CHOICES,
                             default='draft')

    highlight = models.BooleanField(default=False)


    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.
    tags = TaggableManager(blank=True)

    def get_absolute_url(self):
        return reverse('projects:project_detail',
                       args=[self.slug])

    class Meta:
       ordering = ('-start_date',)

    def __str__(self):
        return self.title
