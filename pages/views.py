from django.views.generic import ListView
from .models import Project


class HomePageView(ListView):
    queryset = Project.objects.filter(publish=True)
    model = Project
    context_object_name = 'project_list'
    template_name = 'home.html'

