from django.views.generic import TemplateView
from .models import Service, Team

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.filter(status=True).order_by('?')
        context['team'] = Team.objects.filter(status=True).order_by('?')
        return context
