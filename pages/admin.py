from django.contrib import admin
from .models import Project, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]


admin.site.register(Project, ProjectAdmin)
