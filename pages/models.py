from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    keywords = models.CharField(max_length=250, blank=True)
    github = models.URLField(blank=True)
    link_demo = models.URLField(blank=True)
    link_live = models.URLField(blank=True)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='project/')

