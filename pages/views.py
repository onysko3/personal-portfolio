from django.shortcuts import render
from .models import Project
from people.models import Person



def home_view(request):
    project_list = Project.objects.prefetch_related('photos').filter(publish=True).order_by('-updated')
    has_project = Project.objects.filter(publish=True).count()
    person = Person.objects.get()
    return render(request, 'home.html', {'project_list': project_list, 'person': person,
                                         'has_project': has_project})
