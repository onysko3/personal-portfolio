from django.views.generic import ListView
from .models import Project


class HomePageView(ListView):
    queryset = Project.objects.prefetch_related('photos').filter(publish=True).order_by('-updated')
    model = Project
    context_object_name = 'project_list'
    template_name = 'home.html'

