from django.contrib import admin

# Register your models here.
from .models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'start_date',
                    'status')
    list_filter = ('status', 'created', 'start_date')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'start_date'
    ordering = ['status', 'start_date']

admin.site.register(Project, ProjectAdmin)