from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import *

# use memcache admin index site
admin.site.index_template = 'memcache_status/admin_index.html'


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
    )
    prepopulated_fields = {'slug': ('title',)}


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created_at']
    list_filter = ['created_at', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
