from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    facebook = models.URLField()
    linkedin = models.URLField()
    github = models.URLField()
    picture = models.ImageField(upload_to='', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)

    def __str__(self):
        return self.first_name
